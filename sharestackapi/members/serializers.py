from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, Group
from rest_framework import serializers

from .models import User, Company


# Django models
class ContentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentType
        fields = ("id", "name", "app_label", "model")


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ("id", "name", "content_type", "codename")


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "name", "permissions")


# Our models
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("id", "password", "last_login", "is_superuser", "username",
                  "first_name", "last_name", "email", "is_staff", "is_active",
                  "date_joined", "url", "gravatar", "activation_token",
                  "reset_password_token", "groups", "user_permissions")


class companySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ("name", "url", "description", "logo", "company_user")
