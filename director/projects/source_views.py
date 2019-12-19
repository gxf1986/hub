import json
import os
import tempfile
import typing
from os import unlink

from allauth.socialaccount.models import SocialApp
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils.html import escape
from django.views import View
from django.views.generic import CreateView, DetailView

from accounts.db_facade import user_is_account_admin
from lib import data_size
from lib.converter_facade import ConverterFacade, ConverterIo, ConverterIoType
from lib.conversion_types import DOCX_MIMETYPES, ConversionFormatId, mimetype_from_path
from lib.google_docs_facade import GoogleDocsFacade
from lib.resource_allowance import account_resource_limit, QuotaName, StorageLimitExceededException, \
    get_subscription_upgrade_text
from lib.social_auth_token import user_social_token, user_github_token
from projects.disk_file_facade import DiskFileFacade
from projects.permission_models import ProjectPermissionType
from projects.project_views import ProjectPermissionsMixin
from projects.source_content_facade import SourceEditContext, SourceContentFacade, make_source_content_facade
from projects.source_models import DiskSource, GoogleDocsSource
from projects.source_operations import strip_directory, utf8_path_join, utf8_basename, \
    utf8_dirname
from .models import Project, DropboxSource, GithubSource
from .source_forms import GithubSourceForm, DiskFileSourceForm, GoogleDocsSourceForm


class SourceCreateView(LoginRequiredMixin, ProjectPermissionsMixin, CreateView):
    """A base class for view for creating new project sources."""

    project_permission_required = ProjectPermissionType.EDIT

    def get_initial(self):
        return {
            'project': self.get_project(self.request.user, self.kwargs['pk'])
        }

    def get_redirect(self, pk: int) -> HttpResponse:
        if self.request.GET.get('directory'):
            return redirect("project_files_path", pk, self.request.GET['directory'])
        else:
            return redirect("project_files", pk)

    def form_valid(self, form):
        """Override to set the project for the `Source` and redirect back to that project."""
        pk = self.kwargs['pk']
        file_source = form.save(commit=False)
        file_source.project = get_object_or_404(Project, pk=pk)
        file_source.save()

        return self.get_redirect(pk)


class FileSourceCreateView(LoginRequiredMixin, ProjectPermissionsMixin, View):
    """A view for creating a new, emtpy local file in the project."""

    form_class = DiskFileSourceForm
    template_name = 'projects/filesource_create.html'
    project_permission_required = ProjectPermissionType.EDIT

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:  # type: ignore
        self.get_project(request.user, pk)

        return self.get_response(request, self.form_class())

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:  # type: ignore
        project = self.get_project(request.user, pk)

        form = self.form_class(request.POST)

        if form.is_valid():
            dff = DiskFileFacade(settings.STENCILA_PROJECT_STORAGE_DIRECTORY, project)

            dff.create_file(utf8_path_join(self.current_directory, form.cleaned_data['path']))

            if self.current_directory:
                return redirect("project_files_path", pk, self.current_directory)
            else:
                return redirect("project_files", pk, )

        return self.get_response(request, form)

    def get_response(self, request: HttpRequest, form: DiskFileSourceForm) -> HttpResponse:
        return render(request,
                      self.template_name,
                      self.get_render_context({
                          'current_directory': self.current_directory,
                          'form': form
                      })
                      )

    @property
    def current_directory(self) -> str:
        return self.request.GET.get('directory', '')


class DropboxSourceCreateView(SourceCreateView):
    """A view for creating a Dropbox project source."""

    model = DropboxSource
    template_name = 'projects/dropboxsource_create.html'


class GithubSourceCreateView(SourceCreateView):
    """A view for creating a Github project source."""

    model = GithubSource
    form_class = GithubSourceForm
    template_name = 'projects/githubsource_create.html'

    def get(self, request, *args, **kwargs) -> HttpResponse:
        github_token = user_github_token(request.user)
        if not github_token:
            social_url = reverse('socialaccount_connections')
            messages.error(request, 'Can not link a Github repository as you do not have a Github account connected to '
                                    'your Stencila Hub account.<br/>Please connect your Github account on the '
                                    '<a href="{}">Account Connections page</a>.'.format(social_url), extra_tags='safe')
            return redirect('project_files', kwargs['pk'])

        return super(GithubSourceCreateView, self).get(request, *args, **kwargs)


class GoogleDocsSourceCreateView(SourceCreateView):
    """A view for creating a Github project source."""

    model = GoogleDocsSource
    form_class = GoogleDocsSourceForm
    template_name = 'projects/googledocssource_create.html'

    def form_valid(self, form: GoogleDocsSourceForm) -> HttpResponse:
        google_app = SocialApp.objects.filter(provider='google').first()

        gdf = GoogleDocsFacade(google_app.client_id, google_app.secret, user_social_token(self.request.user, 'google'))

        directory = self.request.GET.get('directory', '')
        document = gdf.get_document(form.cleaned_data['doc_id'])

        pk = self.kwargs['pk']
        source = form.save(commit=False)
        source.project = get_object_or_404(Project, pk=pk)
        source.path = utf8_path_join(directory, document['title'])
        source.save()

        return self.get_redirect(pk)


class FileSourceUploadView(LoginRequiredMixin, ProjectPermissionsMixin, DetailView):
    """A view for uploading one or more files into the project."""

    model = Project
    template_name = 'projects/filesource_upload.html'
    project_permission_required = ProjectPermissionType.EDIT

    def get_context_data(self, **kwargs):
        self.get_project(self.request.user, self.kwargs['pk'])
        context_data = super().get_context_data(**kwargs)
        context_data['upload_directory'] = self.request.GET.get('directory', '')
        return context_data

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:  # type: ignore
        project = self.get_project(request.user, pk)

        directory = request.GET.get('directory', '')
        files = request.FILES.getlist('file')

        dff = DiskFileFacade(settings.STENCILA_PROJECT_STORAGE_DIRECTORY, project)

        storage_limit = typing.cast(int, account_resource_limit(project.account, QuotaName.STORAGE_LIMIT))
        actual_storage_used = storage_used = 0 if storage_limit == -1 else dff.get_project_directory_size()

        respond_with_json = request.META.get('HTTP_ACCEPT') == 'application/json'

        error = None

        try:
            if directory:
                dff.create_directory(directory)

            if storage_limit != -1:
                for file in files:
                    storage_used += file.size
                    if storage_used > storage_limit:
                        plural = 's' if len(files) != 1 else ''
                        raise StorageLimitExceededException(
                            'The file{} could not be saved as it would exceed the storage limit for the account "{}". '
                            'The current limit is {}, you have used {}. Please visit the Account Subscriptions page '
                            'to add or upgrade a subscription'.format(
                                plural, project.account, data_size.to_human(storage_limit),
                                data_size.to_human(actual_storage_used))
                        )

            for file in files:
                dff.write_file_content(utf8_path_join(directory, file.name), file.read())
        except Exception as e:
            if respond_with_json:
                error = str(e)
            else:
                messages.error(request, 'Error during upload: {}'.format(str(e)))

        response_status = 500 if error else (200 if respond_with_json else 204)  # 240 == no content

        if respond_with_json:
            return JsonResponse({
                'success': error is None,
                'error': error
            }, status=response_status)
        else:
            return HttpResponse(status=response_status)


class ContentFacadeMixin(object):
    def get_content_facade(self, request: HttpRequest, project_pk: int, pk: int, path: str) -> SourceContentFacade:
        source = self.get_source(request.user, project_pk, pk)  # type: ignore
        return make_source_content_facade(request.user, path, source,
                                          self.get_project(request.user, project_pk))  # type: ignore


class SourceDownloadView(ProjectPermissionsMixin, ContentFacadeMixin, View):
    project_permission_required = ProjectPermissionType.VIEW

    def get(self, request: HttpRequest, project_pk: int, pk: int, path: str) -> HttpResponse:  # type: ignore
        content_facade = self.get_content_facade(request, project_pk, pk, path)
        return self.process_get(project_pk, path, content_facade)

    def process_get(self, project_pk: int, path: str, content_facade: SourceContentFacade) -> HttpResponse:
        file_content = content_facade.get_binary_content()

        if content_facade.error_exists:
            content_facade.add_messages_to_request(self.request)

            dirname = utf8_dirname(path)

            if dirname:
                return redirect('project_files_path', project_pk, dirname)
            return redirect('project_files', project_pk)

        response = HttpResponse(file_content, content_type='application/octet-stream')

        response['Content-Disposition'] = 'attachment; filename={}'.format(content_facade.get_name())
        return response


class SourceOpenView(LoginRequiredMixin, ProjectPermissionsMixin, ContentFacadeMixin, DetailView):
    project_permission_required = ProjectPermissionType.VIEW

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['file_content'] = self.object.pull()
        return data

    def render(self, request: HttpRequest, editing_context: SourceEditContext,
               extra_context: typing.Optional[dict] = None) -> HttpResponse:
        render_context = {
            'project': self.project,
            'has_edit_permission': self.has_permission(ProjectPermissionType.EDIT),
            'file_name': utf8_basename(editing_context.path),
            'file_directory': utf8_dirname(editing_context.path),
            'file_path': editing_context.path,
            'file_extension': editing_context.extension,
            'file_content': editing_context.content,
            'file_editable': editing_context.editable,
            'source': editing_context.source,
            'supports_commit_message': editing_context.supports_commit_message
        }
        render_context.update(extra_context or {})
        return render(request, 'projects/source_open.html', self.get_render_context(render_context))

    @staticmethod
    def get_default_commit_message(request: HttpRequest):
        return 'Commit from Stencila Hub User {}'.format(request.user)

    def process_get(self, request: HttpRequest, project_pk: int, path: str,
                    content_facade: SourceContentFacade) -> HttpResponse:
        edit_context = content_facade.get_edit_context()

        if edit_context is None:
            content_facade.add_messages_to_request(request)
            dirname = utf8_dirname(path)

            if dirname:
                return redirect('project_files_path', project_pk, dirname)
            return redirect('project_files', project_pk)

        return self.render(request, edit_context, {
            'default_commit_message': self.get_default_commit_message(request)
        })

    def get(self, request: HttpRequest, project_pk: int, pk: int, path: str) -> HttpResponse:  # type: ignore
        content_facade = self.get_content_facade(request, project_pk, pk, path)
        return self.process_get(request, project_pk, path, content_facade)

    @staticmethod
    def get_github_repository_path(source, file_path):
        repo_path = utf8_path_join(source.subpath, strip_directory(file_path, source.path))
        return repo_path

    def post(self, request: HttpRequest, project_pk: int, pk: int, path: str) -> HttpResponse:  # type: ignore
        self.pre_post_check(request, project_pk)

        content_facade = self.get_content_facade(request, project_pk, pk, path)
        return self.perform_post(request, project_pk, path, content_facade)

    def pre_post_check(self, request: HttpRequest, project_pk: int) -> None:
        self.perform_project_fetch(request.user, project_pk)
        if not self.has_permission(ProjectPermissionType.EDIT):
            raise PermissionDenied

    def perform_post(self, request: HttpRequest, project_pk: int, path: str,
                     content_facade: SourceContentFacade) -> HttpResponse:
        commit_message = request.POST.get('commit_message') or self.get_default_commit_message(request)

        storage_limit = account_resource_limit(self.project.account, QuotaName.STORAGE_LIMIT)

        update_success = None
        content_override = None

        if storage_limit != -1 and isinstance(content_facade.source, DiskSource):
            old_size = content_facade.get_size()
            new_size = len(request.POST['file_content'])
            if new_size > old_size:
                storage_used = content_facade.disk_file_facade.get_project_directory_size()
                is_account_admin = user_is_account_admin(self.request.user, self.project.account)
                subscription_upgrade_text = get_subscription_upgrade_text(is_account_admin, self.project.account)

                if (new_size - old_size) + storage_used > storage_limit:
                    message = 'The file content could not be saved as it would exceed the storage limit for the ' \
                              'account <em>{}</em>. {}'.format(escape(self.project.account), subscription_upgrade_text)
                    messages.error(request, message, extra_tags='safe')
                    update_success = False
                    content_override = request.POST['file_content']

        if update_success is None:
            update_success = content_facade.update_content(request.POST['file_content'], commit_message)

        error_exists = content_facade.error_exists

        content_facade.add_messages_to_request(request)

        if error_exists or not update_success:
            edit_context = content_facade.get_edit_context(content_override)

            if edit_context is None or content_facade.error_exists:
                content_facade.add_messages_to_request(self.request)

                dirname = utf8_dirname(path)

                if dirname:
                    return redirect('project_files_path', project_pk, dirname)
                return redirect('project_files', project_pk)

            return self.render(request, edit_context, {
                'commit_message': commit_message,
                'default_commit_message': self.get_default_commit_message(request)
            })

        messages.success(request, 'Content of {} updated.'.format(os.path.basename(path)))
        directory = os.path.dirname(path)
        if directory:
            reverse_name = 'project_files_path'
            args = (project_pk, directory,)  # type: ignore
        else:
            reverse_name = 'project_files'
            args = (project_pk,)  # type: ignore
        return redirect(reverse(reverse_name, args=args))


class DiskFileSourceDownloadView(SourceDownloadView):
    def get(self, request: HttpRequest, project_pk: int, path: str) -> HttpResponse:  # type: ignore
        content_facade = self.get_content_facade(request, project_pk, -1, path)
        return self.process_get(project_pk, path, content_facade)

    def get_content_facade(self, request: HttpRequest, project_pk: int, pk: int, path: str) -> SourceContentFacade:
        return make_source_content_facade(request.user, path, DiskSource(), self.get_project(request.user, project_pk))


class DiskFileSourceOpenView(SourceOpenView):
    project_permission_required = ProjectPermissionType.VIEW

    def get_content_facade(self, request: HttpRequest, project_pk: int, pk: int, path: str) -> SourceContentFacade:
        return make_source_content_facade(request.user, path, DiskSource(), self.get_project(request.user, project_pk))

    def get(self, request: HttpRequest, project_pk: int, path: str) -> HttpResponse:  # type: ignore
        content_facade = self.get_content_facade(request, project_pk, -1, path)
        return self.process_get(request, project_pk, path, content_facade)

    def post(self, request: HttpRequest, project_pk: int, path: str) -> HttpResponse:  # type: ignore
        self.pre_post_check(request, project_pk)

        content_facade = self.get_content_facade(request, project_pk, -1, path)

        return self.perform_post(request, project_pk, path, content_facade)


class DiskFileSourceUpdateView(LoginRequiredMixin, ProjectPermissionsMixin, View):
    form_class = DiskFileSourceForm
    template_name = 'projects/source_update.html'
    project_permission_required = ProjectPermissionType.EDIT

    def get(self, request: HttpRequest, pk: int, path: str) -> HttpResponse:  # type: ignore
        project = self.get_project(request.user, pk)

        form = self.form_class(initial={'path': path})

        dff = DiskFileFacade(settings.STENCILA_PROJECT_STORAGE_DIRECTORY, project)

        if not dff.item_exists(path):
            raise Http404

        return self.get_response(request, project, form, path)

    def get_response(self, request: HttpRequest, project: Project, form: DiskFileSourceForm, path: str) -> HttpResponse:
        return render(request, self.template_name, {
            'project': project,
            'current_path': path,
            'form': form
        })

    def post(self, request: HttpRequest, pk: int, path: str) -> HttpResponse:  # type: ignore
        project = self.get_project(request.user, pk)

        form = self.form_class(request.POST, initial={'path': path})

        dff = DiskFileFacade(settings.STENCILA_PROJECT_STORAGE_DIRECTORY, project)

        if not dff.item_exists(path):
            raise Http404

        if form.is_valid():
            dff.move_file(path, form.cleaned_data['path'])
            messages.success(request, '"{}" was moved to "{}".'.format(path, form.cleaned_data['path']))

            directory = request.GET.get('from', '')

            if directory:
                return redirect('project_files_path', pk, directory)
            else:
                return redirect('project_files', pk)

        return self.get_response(request, project, form, path)


class DiskFileSourceDeleteView(LoginRequiredMixin, ProjectPermissionsMixin, View):
    template_name = 'confirm_delete.html'
    project_permission_required = ProjectPermissionType.EDIT

    def get(self, request: HttpRequest, pk: int, path: str) -> HttpResponse:  # type: ignore
        project = self.get_project(request.user, pk)

        dff = DiskFileFacade(settings.STENCILA_PROJECT_STORAGE_DIRECTORY, project)

        if not dff.item_exists(path):
            messages.warning(request, '{} does not exist in this project.'.format(path))
            return self.get_completion_redirect(pk)

        return render(request, self.template_name, {
            'object': path
        })

    def post(self, request: HttpRequest, pk: int, path: str) -> HttpResponse:  # type: ignore
        project = self.get_project(request.user, pk)

        dff = DiskFileFacade(settings.STENCILA_PROJECT_STORAGE_DIRECTORY, project)

        if not dff.item_exists(path):
            messages.warning(request, '{} does not exist in this project.'.format(path))
            return self.get_completion_redirect(pk)

        dff.remove_item(path)
        messages.success(request, '{} was deleted.'.format(path))

        return self.get_completion_redirect(pk)

    def get_completion_redirect(self, pk: int) -> HttpResponse:
        if self.current_directory:
            return redirect('project_files_path', pk, self.current_directory)

        return redirect('project_files', pk)

    @property
    def current_directory(self) -> str:
        return self.request.GET.get('from', '')


class ConverterMixin:
    _converter: typing.Optional[ConverterFacade] = None

    @property
    def converter(self) -> ConverterFacade:
        if self._converter is None:
            self._converter = ConverterFacade(settings.STENCILA_BINARY)

        return self._converter

    def do_conversion(self, source_type: ConversionFormatId,
                      source_path: str,
                      target_type: ConversionFormatId,
                      target_path: typing.Optional[str] = None) -> str:
        """
        Perform a conversion (with Encoda).

        If `target_path` is not set then a `NamedTemporaryFile` is created and its path returned. The temporary file
        is not cleaned up.
        """
        if not target_path:
            with tempfile.NamedTemporaryFile(delete=False) as temp_output:
                target_path = temp_output.name

        converter_input = ConverterIo(ConverterIoType.PATH, source_path, source_type)
        converter_output = ConverterIo(ConverterIoType.PATH, target_path, target_type)

        convert_result = self.converter.convert(converter_input, converter_output, None)

        if convert_result.returncode != 0:
            raise RuntimeError('Convert process failed. Stderr is: {}'.format(
                convert_result.stderr.decode('ascii')))

        return target_path

    def convert_to_google_docs(self, request: HttpRequest, project: Project, scf: SourceContentFacade, target_name: str,
                               target_path: str) -> None:
        """
        Convert a document to Google Docs.

        If the document is already in DOCX or HTML format it will just be uploaded, otherwise it is first converted to
        DOCX. The document is uploaded in DOCX/HTML and Google takes care of converting to Google Docs format.
        """
        if scf.source_type not in (ConversionFormatId.html, ConversionFormatId.docx):
            output_content, output_mime_type = self.convert_source_for_google_docs(scf)
        else:
            output_mime_type = mimetype_from_path(scf.file_path) or 'application/octet-stream'
            output_content = scf.get_binary_content()
        gdf = scf.google_docs_facade

        if gdf is None:
            raise TypeError('Google Docs Facade was not set up. Check that app tokens are good.')

        new_doc_id = gdf.create_document(target_name, output_content, output_mime_type)
        existing_source = GoogleDocsSource.objects.filter(project=project, path=target_path).first()
        new_source = gdf.create_source_from_document(project, utf8_dirname(target_path), new_doc_id)
        if existing_source is not None:
            gdf.trash_document(existing_source.doc_id)
            messages.info(request, 'Existing Google Docs file "{}" was moved to the Trash.'.format(target_name))
            existing_source.doc_id = new_source.doc_id
            existing_source.save()
        else:
            new_source.save()

    def convert_source_for_google_docs(self, scf: SourceContentFacade) -> typing.Tuple[bytes, str]:
        # GoogleDocs can only convert from HTML or DOCX so convert to DOCX on our end first
        temp_output_path = None
        input_path = None
        # if the source is not from Disk then the content should be saved to a temp path beforehand
        use_temp_input_path = not isinstance(scf.source, DiskSource)
        try:
            input_path = scf.sync_content(use_temp_input_path)

            temp_output_path = self.do_conversion(scf.source_type, input_path, ConversionFormatId.docx)

            with open(temp_output_path, 'r+b') as temp_output:  # reopen after data has been written
                output_content = temp_output.read()  # this is in DOCX after conversion
        finally:
            if use_temp_input_path and input_path:
                unlink(input_path)

            if temp_output_path:
                unlink(temp_output_path)
        return output_content, DOCX_MIMETYPES[0]

    def source_convert(self, request: HttpRequest, project: Project, scf: SourceContentFacade, target_path: str,
                       target_name: str, target_type: ConversionFormatId) -> None:
        if target_type == ConversionFormatId.gdoc:
            self.convert_to_google_docs(request, project, scf, target_name, target_path)
        else:
            absolute_input_path = scf.sync_content()
            absolute_output_path = scf.disk_file_facade.full_file_path(target_path)

            self.do_conversion(scf.source_type, absolute_input_path, target_type, absolute_output_path)


class SourceConvertView(LoginRequiredMixin, ProjectPermissionsMixin, ConverterMixin, View):
    project_permission_required = ProjectPermissionType.EDIT

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:  # type: ignore
        project = self.get_project(request.user, pk)

        body = json.loads(request.body)

        source_id = body['source_id']
        source_path = body['source_path']
        target_id = body['target_type']
        target_name = body['target_name']

        if '/' in target_name:
            raise ValueError('Target name can not contain /')

        source = self.get_source(request.user, pk, source_id)
        scf = make_source_content_facade(request.user, source_path, source, project)

        target_path = utf8_path_join(utf8_dirname(source_path), target_name)
        target_type = ConversionFormatId.from_id(target_id)

        self.source_convert(request, project, scf, target_path, target_name, target_type)

        for message in scf.message_iterator():
            messages.add_message(request, message.level, message.message)

        messages.success(request, '{} was converted.'.format(utf8_basename(source_path)))

        return JsonResponse({
            'success': True
        })


67
