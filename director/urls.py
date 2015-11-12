"""director URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))

Some of the URLs below include non-alphanumeric characters (e.g. !, &).
Note that http://www.ietf.org/rfc/rfc3986.txt (section 2.2) says that 'reserved' characters
"may (or may not) be defined as delimiters by the generic syntax, by each
scheme-specific syntax, or by the implementation-specific syntax of a URI's dereferencing algorithm"
So, it seems fine to use these characters
  unreserved = ALPHA / DIGIT / "-" / "." / "_" / "~"
  reserved sub-delims = "!" / "$" / "&" / "'" / "(" / ")" / "*" / "+" / "," / ";" / "="
But probably best to avoid these:
  reserved gen-delims  = ":" / "/" / "?" / "#" / "[" / "]" / "@"
because they are used as general delimiters in the URI generic syntax

"""
from django.conf.urls import url, include
from django.contrib import admin

import general.views
import components.views

urlpatterns = [
    # API endpoints
    url(r'^api/v1/',                                                 include('api_v1')),

    # API documentation
    url(r'^api/api.yml',                                             general.views.api_yml),
    url(r'^api/?$',                                                  general.views.api_ui),

    # User management (login, logout etc)
    url(r'^me/',                                                     include('allauth.urls')),

    # Administration interface
    url(r'^admin/',                                                  admin.site.urls),

    # Test views
    url(r'^test/400',                                                general.views.test400),
    url(r'^test/403',                                                general.views.test403),
    url(r'^test/404',                                                general.views.test404),
    url(r'^test/500',                                                general.views.test500),
]

urlpatterns += [
    # Slugified URL
    url(r'^(?P<address>.+)/(?P<slug>.*)-$',                          components.views.slugified),

    # Tiny URL e.g.
    #   /gdf3Nd~
    # Gets redirected to the canonical URL for the component
    # The tilde prevents potential (although low probability)
    # clashes between shortened URLs and other URLs
    url(r'^(?P<tiny>\w+)~$',                                         components.views.tiny),

    # Component Git repo access: distinguished by `.git` followed by query
    url(r'^(?P<address>.+)\.git.*$',                                 components.views.git),

    # Component raw file access: any other url with a dot in it (resolved in view)
    url(r'^(?P<path>(.+)\.(.+))$',                                   components.views.raw),

    # Any other URL needs to be routed to the a canonical URL, index page, or
    # listing of components at the address
    url(r'^(?P<address>.*)$',                                        components.views.route),
]