from rest_framework.serializers import ModelSerializer

from normalizr import NormalizrSerializer
from projects.project_models import Project


class ProjectListSerializer(NormalizrSerializer):
    entity_plural = 'projects'


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name')
        list_serializer_class = ProjectListSerializer
