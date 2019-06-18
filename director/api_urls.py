from django.urls import path, include
from users.api_v1_urls import urlpatterns as user_v1_patterns
from projects.api_v1_urls import urlpatterns as project_v1_patterns

urlpatterns = [
    path('v1/', include([
        path('rest-auth/', include('rest_auth.urls')),
        path('users/', include(user_v1_patterns)),
        path('projects/', include(project_v1_patterns))
    ]))
]
