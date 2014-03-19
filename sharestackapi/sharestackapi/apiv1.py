from django.conf.urls import patterns, url, include
from rest_framework import routers

from members import views as member_views


router = routers.DefaultRouter()
router.register(r'users', member_views.UserViewSet)


urlpatterns = patterns('',

    url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls',
                namespace='rest_framework')
        )
)
