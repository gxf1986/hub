import json
import typing

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from rest_framework import generics, permissions, views
from rest_framework.exceptions import APIException
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.utils.encoders import JSONEncoder

from lib.social_auth_token import user_github_token
from projects.permission_facade import fetch_project_for_user
from projects.permission_models import ProjectPermissionType
from projects.project_models import Project
from projects.project_views import ProjectPermissionsMixin
from projects.serializers import ProjectSerializer, SERIALIZER_LOOKUP
from projects.source_models import AvailableSourceType, LinkedSourceAuthentication
from projects.source_operations import list_project_directory


class StencilaJSONEncoder(JSONEncoder):
    """
    Call the `to_json` method on an object (if one exists) to encode the object.

    If no `to_json` method exists then fall back to the default encoding methods.
    """

    def default(self, o: typing.Any) -> typing.Any:
        if hasattr(o, 'to_json'):
            return o.to_json()

        return super().default(o)


class StencilaJSONRenderer(JSONRenderer):
    encoder_class = StencilaJSONEncoder


class ProjectDetailView(ProjectPermissionsMixin, View):
    # Old style, not using DRF. Should be deprecated
    project_permission_required = ProjectPermissionType.VIEW

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        project = self.get_project(request.user, pk)

        if not self.has_permission(ProjectPermissionType.MANAGE):
            raise PermissionDenied('You do not have permission to edit this Project.')

        update_data = json.loads(request.body)

        project_updated = False

        for key, value in update_data.items():
            if not hasattr(project, key):
                raise ValueError('Invalid update data key: "{}".'.format(key))

            setattr(project, key, value)
            project_updated = True

        if project_updated:
            project.save()

        return JsonResponse(
            {'success': True}
        )


class ProjectListView(generics.ListAPIView):
    """List all projects that the logged in user has created."""

    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Project.objects.filter(creator=self.request.user)


class UnknownSourceTypeException(APIException):
    status_code = 400
    default_detail = 'The requested source type is not known.'
    default_code = 'unknown_source_type'


class LinkedSourcesListView(generics.ListCreateAPIView):
    """List all Sources for a particular Project."""

    permission_classes = (permissions.IsAuthenticated,)

    def get_source_type_id(self) -> typing.Optional[str]:
        return self.request.GET.get('type')

    def get_serializer_class(self, *args: list, **kwargs: dict) -> typing.Type[ModelSerializer]:
        source_type = self.get_source_type_id()
        try:
            return SERIALIZER_LOOKUP[source_type]
        except KeyError:
            raise UnknownSourceTypeException()

    def get_queryset(self):
        project_fetch_result = fetch_project_for_user(self.request.user, self.kwargs['pk'], True)
        try:
            source_model = AvailableSourceType.model_lookup(self.get_source_type_id())
        except KeyError:
            raise UnknownSourceTypeException()
        return source_model.objects.filter(project=project_fetch_result.project)

    def create(self, request: Request, *args: list, **kwargs: dict) -> HttpResponse:
        project_fetch_result = fetch_project_for_user(self.request.user, self.kwargs['pk'], True)

        if ProjectPermissionType.EDIT not in project_fetch_result.agent_permissions:
            raise PermissionDenied

        return super(LinkedSourcesListView, self).create(request, *args, **kwargs)


class SourcesListView(views.APIView):
    """List all Sources (including Files) in a particular directory, for a Project."""

    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = (StencilaJSONRenderer, BrowsableAPIRenderer)

    def get(self, request: Request, pk: int, directory: typing.Optional[str] = None):
        project_fetch_result = fetch_project_for_user(self.request.user, pk, True)

        authentication = LinkedSourceAuthentication(user_github_token(request.user))

        directory_entries = list_project_directory(settings.STENCILA_PROJECT_STORAGE_DIRECTORY,
                                                   project_fetch_result.project, authentication, directory)
        return Response(directory_entries)
