'''
Defines some common, "general" views not tied to a specific app.
'''
import json
from collections import OrderedDict

from django.template import Context, loader
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError
from django.http import Http404
from django.core.exceptions import SuspiciousOperation, PermissionDenied
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder

from components.models import Component
from general.api import API

def front(request):
    '''
    Front page at /
    '''
    components = Component.list(
        user=request.user,
        published=True,
        sort='-id'
    )
    return render(request, 'front.html', {
        'components': components
    })


# API documentation

def api_ui(request):
    '''
    Render API documentation template based on Swagger UI but with
    header and footer etc
    '''
    return render(request, 'api.html')


def api_yml(request):
    '''
    Render API Swagger specification. This is templated
    to allow for the UI to be used in local development mode
    '''
    return render(request, 'api.yml')


# Custom error views
#  See https://docs.djangoproject.com/en/1.9/topics/http/views/#customizing-error-views
# At time of writing, 400, 403, 404 and 500 are the only codes which have custom handling

def render_error(request, template):
    template = loader.get_template(template)
    try:
        sentry_id = request.sentry['id']
    except:
        sentry_id = None
    data = dict(
        uri=request.build_absolute_uri(),
        remote=request.META.get('REMOTE_ADDR'),
        sentry_id=sentry_id
    )
    return template.render({
        'comment_end': '-->',
        'comment_begin': '<!--',
        'data': json.dumps(data, cls=DjangoJSONEncoder, indent=4),
        'sentry_id': sentry_id
    })

def handler400(request):
    '''
    Bad request handler
    '''
    return HttpResponseBadRequest(render_error(request, '4xx.html'))


def handler403(request):
    '''
    Permission denied handler
    '''
    return HttpResponseForbidden(render_error(request, '403.html'))


def handler404(request):
    '''
    Not found handler
    '''
    return HttpResponseNotFound(render_error(request, '404.html'))


def handler500(request):
    '''
    Server error handler.
    Includes `request` in the context so that a Sentry case reference id can be reported.
    '''
    return HttpResponseServerError(render_error(request, '5xx.html'))


# Test error views are used to test that the correct templates
# are being used for errors and that error reporting (currently via Sentry)(
# is behaving as intended.


@staff_member_required
def test400(request):
    raise SuspiciousOperation('You should see this in DEBUG mode but in production see a custom 400 page')


@staff_member_required
def test403(request):
    raise PermissionDenied()


@staff_member_required
def test404(request):
    raise Http404()


@staff_member_required
def test500(request):
    # Supposdly a SystemExist exception is ignored by the test client - but it wasn't for me
    # https://docs.djangoproject.com/en/1.7/topics/testing/tools/#exceptions
    # A plain old exception at least gets reportest in the debugger
    raise Exception('Faked server error')


def test_user_agent(request):
    '''
    For testing what django-user-agents and our internal request handler
    is returning for different, ummm, user agents
    '''
    rh = API(request)
    ua = request.user_agent
    return rh.respond(OrderedDict([
        ('rh_accept', rh.accept),
        ('rh_browser', rh.browser),
        ('ua_is_mobile', ua.is_mobile),
        ('ua_is_tablet', ua.is_tablet),
        ('ua_is_touch_capable', ua.is_touch_capable),
        ('ua_is_pc', ua.is_pc),
        ('ua_is_bot', ua.is_bot),
        ('ua_browser', ua.browser),
        ('ua_browser_family', ua.browser.family),
        ('ua_browser_version', ua.browser.version),
        ('ua_browser_version_string', ua.browser.version_string),
        ('ua_os', ua.os),
        ('ua_os_family', ua.os.family),
        ('ua_os_version', ua.os.version),
        ('ua_os_version_string', ua.os.version_string),
        ('ua_device', ua.device),
        ('ua_device_family', ua.device.family),
    ]))


def backend_error(request, backend, url):
    '''
    Used to capture and report backend requests to Sentry.
    Only intended to be called internally by Nginx.
    Hence the REMOTE_ADDR header requirement.
    '''
    if request.META.get('REMOTE_ADDR') != '127.0.0.1':
        return HttpResponseForbidden()
    raise BackendError('%s : %s' % (backend, url))


class BackendError(Exception):
    pass
