from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, Group
from rest_framework import viewsets

from .models import User, Company
from .serializers import (UserSerializer,
                          PermissionSerializer,
                          GroupSerializer,
                          ContentTypeSerializer,
                          CompanySerializer)


class ContentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Content type django model to be viewed or edited.
    """
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows permissions django model to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows group django model to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Company to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer