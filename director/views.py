from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView, RedirectView

from lib.browser_detection import user_agent_is_internet_explorer


class HomeView(View):
    """
    Home page view.

    Served at /. Redirects to other urls depending on whether
    the user is authenticated or not.
    """

    def get(self, request: HttpRequest, *args, **kwargs):
        # Send OK to Google's health checker which always hits "/"
        # despite settings to the contrary.
        # This is a known bug being tracked here:
        # https://github.com/kubernetes/ingress-gce/issues/42
        # https://github.com/ory/k8s/issues/113#issuecomment-596281449
        user_agent = request.META.get("HTTP_USER_AGENT", "")
        if "GoogleHC" in user_agent:
            return HttpResponse("OK")

        # Redirect to secure version. This needs to be done here to
        # avoid sending a 302 to GoogleHC.
        if settings.SECURE_SSL_REDIRECT and not request.is_secure():
            return redirect("https://" + request.get_host() + "/")

        # Authenticated users get redirected to the user dashboard
        if self.request.user.is_authenticated:
            return redirect("ui-user-dashboard")

        # Unauthenticated users get redirected to /open
        return redirect("open_main")


class AboutView(TemplateView):
    """Page displaying short overview of the Hub."""

    template_name = "about/about.html"


class ContactView(TemplateView):
    """Page displaying contact information."""

    template_name = "about/contact.html"


class HelpView(TemplateView):
    """Page displaying help."""

    template_name = "about/help.html"


class IcoView(RedirectView):
    permanent = True
    url = "/static/img/favicon.ico"


class Test403View(View):
    """
    A 403 view to test 403 error.

    This view allows testing of 403 error handling in production
    (ie. test that custom 403 page is displayed)
    """

    def get(self, request):
        raise PermissionDenied("This is a test 403 error")


class Test404View(View):
    """
    A 404 view to test 404 error.

    This view allows testing of 404 error handling in production
    (ie. test that custom 404 page is displayed)
    """

    def get(self, request):
        raise Http404("This is a test 404 error")


class Test500View(View):
    """
    A 500 view to test 500 error.

    This view allows testing of 500 error handling in production (e.g that stack traces are
    being sent to Sentry). Can only be run by staff.
    """

    @method_decorator(staff_member_required)
    def get(self, request):
        raise RuntimeError("This is a test error")


class IeUnsupportedView(View):
    """A view to let users know that we don't support Internet Explorer (yet)."""

    def get(self, request: HttpRequest) -> HttpResponse:
        if not user_agent_is_internet_explorer(request.META.get("HTTP_USER_AGENT")):
            return redirect("/")

        return render(request, "ie-unsupported.html")
