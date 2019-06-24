import json
import logging
import typing

from allauth.socialaccount.models import SocialApp
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.generic.base import View

from django.conf import settings
from googleapiclient.errors import HttpError

from lib.google_docs_facade import extract_google_document_id_from_url, google_document_id_is_valid, GoogleDocsFacade
from lib.social_auth_token import user_social_token
from projects.disk_file_facade import DiskFileFacade, ItemType
from projects.permission_models import ProjectPermissionType
from projects.project_views import ProjectPermissionsMixin
from projects.source_models import GoogleDocsSource
from projects.source_operations import utf8_path_join

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class LinkException(Exception):
    pass


class MissingTokenException(LinkException):
    pass


class DiskItemCreateView(ProjectPermissionsMixin, View):
    project_permission_required = ProjectPermissionType.EDIT

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        project = self.get_project(request.user, pk)

        dff = DiskFileFacade(settings.STENCILA_PROJECT_STORAGE_DIRECTORY, project)

        body = json.loads(request.body)

        item_type = ItemType(body['type'])
        path = body['path']

        error = None

        if dff.item_exists(path):
            error = 'Item exists at "{}".'.format(path)
        elif item_type == ItemType.FILE:
            dff.create_file(path)
        elif item_type == ItemType.FOLDER:
            dff.create_directory(path)
        else:
            raise TypeError('Don\'t know how to create a {}'.format(item_type))

        return JsonResponse(
            {
                'success': not error,
                'error': error
            }
        )


class DiskItemMoveView(ProjectPermissionsMixin, View):
    project_permission_required = ProjectPermissionType.EDIT

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        project = self.get_project(request.user, pk)

        dff = DiskFileFacade(settings.STENCILA_PROJECT_STORAGE_DIRECTORY, project)

        body = json.loads(request.body)

        source = body['source']
        destination = body['destination']

        error = None

        if not dff.item_exists(source):
            error = 'Source item does not exist at "{}".'.format(source)
        elif dff.item_exists(destination):
            error = 'Destination already exists at "{}".'.format(destination)
        else:
            dff.move_file(source, destination)

        return JsonResponse({
            'success': not error,
            'error': error
        })


class DiskItemRemoveView(ProjectPermissionsMixin, View):
    project_permission_required = ProjectPermissionType.EDIT

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        project = self.get_project(request.user, pk)

        dff = DiskFileFacade(settings.STENCILA_PROJECT_STORAGE_DIRECTORY, project)

        body = json.loads(request.body)

        path = body['path']

        error = None

        if not dff.item_exists(path):
            error = 'Item does not exist at "{}".'.format(path)
        else:
            dff.remove_item(path)

        return JsonResponse({
            'success': not error,
            'error': error
        })


class SourceLinkView(ProjectPermissionsMixin, View):
    project_permission_required = ProjectPermissionType.EDIT

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        self.get_project(request.user, pk)

        body = json.loads(request.body)

        source_type = body['source_type']

        error = None
        error_code = None
        custom_status = None

        if source_type == 'gdoc':
            try:
                self.link_google_doc(request.user, body['document_id'], body['directory'])
            except MissingTokenException as e:
                error_code = 'MISSING_TOKEN'
                error = str(e)
                custom_status = 401
            except LinkException as e:
                error_code = 'LINK_ERROR'
                error = str(e)
        else:
            error = 'Unknown source type {}'.format(source_type)

        return JsonResponse({
            'success': not error,
            'error': error,
            'error_code': error_code
        }, status=custom_status)

    def link_google_doc(self, user: User, doc_id: str, directory: str) -> None:
        cleaned_doc_id, document = load_google_doc(user, doc_id)

        source = GoogleDocsSource(doc_id=cleaned_doc_id)

        source.project = self.project
        source.path = utf8_path_join(directory, document['title'])
        source.save()


def load_google_doc(user: User, doc_id: str) -> typing.Tuple[str, dict]:
    token = user_social_token(user, 'google')
    if token is None:
        raise MissingTokenException('Can\'t link as no Google account is connected to this Stencila Hub account.')
    if not doc_id:
        raise LinkException('A document ID or URL was not provided.')
    try:
        cleaned_doc_id = extract_google_document_id_from_url(doc_id)
    except ValueError:
        cleaned_doc_id = doc_id  # not a URL, could just a be the ID

    if not google_document_id_is_valid(cleaned_doc_id):
        raise LinkException('"{}" is not a valid Google Document ID.'.format(cleaned_doc_id))
    google_app = SocialApp.objects.filter(provider='google').first()
    gdf = GoogleDocsFacade(google_app.client_id, google_app.secret, token)
    try:
        document = gdf.get_document(cleaned_doc_id)
    except HttpError:
        logger.exception("Error fetching google doc {}".format(cleaned_doc_id))
        raise LinkException('Could not retrieve the document, please check the ID/URL.')

    return cleaned_doc_id, document
