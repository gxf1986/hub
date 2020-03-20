from django.urls import path, include
from django.views.generic import TemplateView

from auth.api_urls import urlpatterns as auth_urls
from projects.api_urls import urlpatterns as project_urls
from users.api_urls import urlpatterns as user_urls

from api_views import schema_view

urlpatterns = [
    # API schema
    path("schema/", schema_view, name="api_schema"),
    # Swagger Docs
    path(
        "docs/", TemplateView.as_view(template_name="api_swagger.html"), name="api_ui"
    ),
    # API URLs for each app
    path("auth/", include(auth_urls)),
    path("projects/", include(project_urls)),
    path("users/", include(user_urls)),
]
