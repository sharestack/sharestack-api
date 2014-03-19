from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import apiv1


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'/'.join(("^api", settings.API_VERSION, "")),
        # DRF has a bug in nested namespaces, doesn't check
        # xxx:yyy-detail namespaces, Only yyy-detail and similar
        # https://github.com/tomchristie/django-rest-framework/pull/1143
        # for now without namespaces, uncomment this line when fixed
        # include(apiv1.urlpatterns, namespace='api')),
        include(apiv1.urlpatterns)),
)
