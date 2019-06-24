from django.urls import path

from projects.source_api_views import DiskItemCreateView, DiskItemMoveView, DiskItemRemoveView, SourceLinkView
from projects.project_api_views import ProjectDetailView, ProjectListView, LinkedSourcesListView, SourcesListView

urlpatterns = [
    path('', ProjectListView.as_view(), name='api_v1_project_list'),
    path('<int:pk>/linked-sources', LinkedSourcesListView.as_view(), name='api_v1_linked_source_list'),
    path('<int:pk>/sources', SourcesListView.as_view(), name='api_v1_source_list'),
    path('<int:pk>/sources/<path:directory>', SourcesListView.as_view(), name='api_v1_source_list'),

    # fake API views for the JS frontend – should be made redundant

    path('<int:pk>', ProjectDetailView.as_view(), name='api_v1_project_detail'),
    path('<int:pk>/item-create', DiskItemCreateView.as_view(), name='api_v1_project_item_create'),
    path('<int:pk>/item-move', DiskItemMoveView.as_view(), name='api_v1_project_item_move'),
    path('<int:pk>/item-remove', DiskItemRemoveView.as_view(), name='api_v1_project_item_remove'),
    path('<int:pk>/sources/link', SourceLinkView.as_view(), name='api_v1_sources_link')
]
