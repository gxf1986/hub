from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.defaults import permission_denied, page_not_found

import checkouts.views
import user_views
import users.views
import views
# specify sub paths as their own patterns to make it easier to see which root paths are defined in urlpatterns
# this will make it easier to keep the DISALLOWED_ACCOUNT_SLUGS up to date
from lib.constants import UrlRoot

about_patterns = [
    path('', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('help/', views.HelpView.as_view(), name='help'),
    path('privacy-policy/', views.PrivacyView.as_view(), name='privacy-policy'),
    path('terms-and-conditions/', views.TermsView.as_view(), name='terms-and-conditions'),
]

# for use with Django TV >_<
test_patterns = [
    path('403/', views.Test403View.as_view()),
    path('404/', views.Test404View.as_view()),
    path('500/', views.Test500View.as_view()),
]

urlpatterns = [
    # All in alphabetical order. Patterns that are fully defined in urlpatterns come first
    # Home page
    path('', user_views.HomeView.as_view(), name='home'),

    # Beta Token Getting View
    path(UrlRoot.beta.value + '/', users.views.BetaTokenView.as_view(), name='user_beta'),

    # ico for old browsers
    path(UrlRoot.favicon.value, views.IcoView.as_view()),

    # Redirect IE users to this view
    path(UrlRoot.ie_unsupported.value + '/', views.IeUnsupportedView.as_view(), name='ie-unsupported'),

    # status
    path(UrlRoot.system_status.value + '/', views.StatusView.as_view()),

    # Patterns that include other urlpatterns or files

    # About pages etc
    path(UrlRoot.about.value + '/', include(about_patterns)),

    # Accounts App
    path(UrlRoot.accounts.value + '/', include('accounts.urls')),

    # Staff (Django) admin
    path(UrlRoot.admin.value + '/', admin.site.urls),

    # API
    path(UrlRoot.api.value + '/', include('api_urls')),

    # Checkouts App
    path(UrlRoot.checkouts.value + '/', include('checkouts.urls')),
    # Shortcut to `checkout_create`
    path(UrlRoot.checkout.value + '/', checkouts.views.CheckoutCreateView.as_view(), name='checkout_create_shortcut'),

    # User sign in, settings etc
    path(UrlRoot.me.value + '/', include('users.urls')),

    # StencilaOpen App
    path(UrlRoot.open.value + '/', include('stencila_open.urls')),

    # Projects App
    path(UrlRoot.projects.value + '/', include('projects.urls')),

    # Stencila Admin App (not Django Admin)
    path(UrlRoot.stencila_admin.value + '/', include('stencila_admin.urls')),

    # Testing errors
    path(UrlRoot.test.value + '/', include(test_patterns)),

    # Custom Roots (they start with a slug)
    path('<slug:account_name>/', include('accounts.slug_urls'))
]

handler403 = permission_denied
handler404 = page_not_found
handler500 = views.error_500_view

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path(UrlRoot.debug.value + '/', include(debug_toolbar.urls)),
                  ] + urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
