from django.conf.urls import patterns, url, include
from rest_framework import routers

from members import views as member_views
from machines import views as machines_views


router = routers.DefaultRouter()

router.register(r'contenttypes', member_views.ContentTypeViewSet)
router.register(r'permissions', member_views.PermissionViewSet)
router.register(r'groups', member_views.GroupViewSet)
router.register(r'users', member_views.UserViewSet)
router.register(r'companies', member_views.CompanyViewSet)

router.register(r'stacks', machines_views.StackViewSet)


urlpatterns = patterns('',

    url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls',
                namespace='rest_framework')
        )
)
