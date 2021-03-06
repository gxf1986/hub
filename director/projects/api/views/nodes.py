import json
import secrets
from typing import Optional

from django.conf import settings
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import (
    mixins,
    parsers,
    permissions,
    renderers,
    serializers,
    status,
    viewsets,
)
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework.request import Request
from rest_framework.response import Response
from stencila.schema.util import node_type

from lib.conversion_types import ConversionFormatId
from lib.converter_facade import (
    ConverterFacade,
    ConverterIo,
    ConverterIoType,
    ConverterContext,
)
from projects.models import Node
from projects.views.mixins import ProjectPermissionsMixin, ProjectPermissionType

# Applications known to create nodes
# For these provide further details in HTML views of nodes
APPS = {
    "api": ("Stencila Hub API", "https://hub.stenci.la/api"),
    "encoda": ("Stencila Encoda", "https://github.com/stencila/encoda#readme"),
    "gsuita": (
        "Stencila for GSuite",
        "https://gsuite.google.com/marketplace/app/stencila/110435422451",
    ),
}


class NodesCreateRequest(serializers.ModelSerializer):
    """The request data when creating a new node."""

    node = serializers.JSONField(required=True, help_text="The node itself.")

    class Meta:
        model = Node
        fields = ["project", "app", "host", "node"]
        ref_name = None


class NodesCreateResponse(serializers.ModelSerializer):
    """The response data when creating a new node."""

    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.get_absolute_url())

    class Meta:
        model = Node
        fields = ["key", "url"]
        ref_name = None


class NodeSerializer(NodesCreateResponse):
    """The response data when retrieving a node."""

    node = serializers.JSONField(source="json", help_text="The node itself.")

    class Meta:
        model = Node
        fields = ["creator", "created", "project", "app", "host", "key", "url", "node"]
        ref_name = None


class NodesViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
    ProjectPermissionsMixin,
):

    # Configuration

    lookup_url_kwarg = "key"

    # Use the plain `JSONParser`, rather than the default
    # `CamelCaseJSONParser` so that camelCased properties within
    # a node are not transformed to snake case.
    parser_classes = [parsers.JSONParser]

    # Use `TemplateHTMLRenderer` as the default renderer so that
    # bots that `Accept` anything get HTML that rather than JSON.
    # For why this ordering is important see
    # https://www.django-rest-framework.org/api-guide/renderers/#ordering-of-renderer-classes
    renderer_classes = [renderers.TemplateHTMLRenderer, renderers.JSONRenderer]

    def get_permissions(self):
        """
        Get the list of permissions that the current action requires.

        - `create` (i.e. POST) required authentication to prevent unauthenticated
          users using this view set as a key/value store
        - `retrieve` (i.e. GET) does not require authentication (although content
          will be limited in that case)
        """
        if self.action == "create":
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    # Views

    @swagger_auto_schema(
        request_body=NodesCreateRequest,
        responses={status.HTTP_201_CREATED: NodesCreateResponse},
    )
    def create(self, request: Request) -> Response:
        """
        Create a node.

        Receives a request with the `node` and other information e.g. `project`.
        Returns the URL of the node.
        """
        serializer = NodesCreateRequest(data=request.data)
        serializer.is_valid(raise_exception=True)

        project = serializer.validated_data.get("project")
        app = serializer.validated_data.get("app", "api")
        host = serializer.validated_data.get("host")
        node = serializer.validated_data.get("node")

        # Check that the user has EDIT permissions for the project,
        # if provided.
        if project and not self.is_permitted(
            request.user, ProjectPermissionType.EDIT, pk=project.id
        ):
            raise PermissionDenied

        # Create the node with a unique key
        node = Node.objects.create(
            creator=request.user,
            key=secrets.token_hex(32),
            project=project,
            app=app,
            host=host,
            json=node,
        )

        serializer = NodesCreateResponse(node, context={"request": request})
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            # Most of the time this action will requested with `Accept: application/json`.
            # However, in case it is not, `template_name` is required.
            template_name="projects/node_complete.html",
        )

    @swagger_auto_schema(responses={status.HTTP_200_OK: NodeSerializer},)
    def retrieve(
        self, request: Request, key: str, format: Optional[str] = None
    ) -> Response:
        """
        Retrieve a node.

        Performs content negotiation and authorization based on the `Accept` header.

        - For `application/json` returns 403 if the request user is not authorized
        to read the project.
        - For `text/html` (and others) returns a very simple HTML rendering of the
        of the node (only type etc) if the user does not have read access to the project.
        Otherwise, should return a full HTML rendering of the node using Encoda.
        """
        node = get_object_or_404(Node, key=key)
        if format == "json" or request.accepted_renderer.format == "json":
            # Require the user is authenticated and has VIEW permissions for the project
            if not request.user.is_authenticated:
                raise NotAuthenticated
            if node.project and not self.is_permitted(
                request.user, ProjectPermissionType.VIEW, pk=node.project.id
            ):
                raise PermissionDenied

            serializer = NodeSerializer(node, context={"request": request})
            return Response(serializer.data)
        else:
            # Return a basic view if the user does NOT have VIEW permissions.
            if node.project and not self.is_permitted(
                request.user, ProjectPermissionType.VIEW, pk=node.project.id
            ):
                return Response(
                    {"node_type": node_type(node.json), "node": node},
                    template_name="projects/node_basic.html",
                )

            # Return a more complete view if the user has VIEW permissions.
            # This should include public projects.
            try:
                # Currently allow this to fail if the converter binary
                # can not be found e.g. during CI testing
                conversion = ConverterFacade(settings.STENCILA_ENCODA_PATH).convert(
                    input_data=ConverterIo(
                        ConverterIoType.PIPE,
                        json.dumps(node.json).encode("utf8"),
                        ConversionFormatId.json,
                    ),
                    output_data=ConverterIo(
                        ConverterIoType.PIPE, None, ConversionFormatId.html
                    ),
                    context=ConverterContext(standalone=False),
                )
                html = conversion.stdout.decode("utf8")
            except FileNotFoundError:
                html = ""

            app_name, app_url = APPS.get(node.app, (node.app, None))
            return Response(
                {
                    "node_type": node_type(node.json),
                    "app_url": app_url,
                    "app_name": app_name,
                    "node": node,
                    "html": html,
                },
                template_name="projects/node_complete.html",
            )
