import typing

from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer, ValidationError

from normalizr import NormalizrSerializer
from projects.project_models import Project
from projects.source_api_views import load_google_doc, LinkException
from projects.source_models import GoogleDocsSource


class UserProjectForeignKey(PrimaryKeyRelatedField):
    def get_queryset(self):
        return Project.objects.filter(creator=self.context['request'].user)


class ProjectListSerializer(NormalizrSerializer):
    entity_plural = 'projects'


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name')
        # list_serializer_class = ProjectListSerializer  # TODO: normalizr serializer all the way down


class GoogleDocsSourceSerializer(ModelSerializer):
    project = UserProjectForeignKey()

    class Meta:
        model = GoogleDocsSource
        fields = ('pk', 'type_id', 'project', 'path', 'doc_id')

    def validate_doc_id(self, value: typing.Optional[str]) -> str:
        if not value:
            raise ValidationError('"doc_id" must be specified')

        try:
            clean_document_id, _ = load_google_doc(self.context['request'].user, value)
        except LinkException as e:
            raise ValidationError(str(e))

        return clean_document_id


SERIALIZER_LOOKUP = {
    GoogleDocsSource.type_id: GoogleDocsSourceSerializer
}
