from .models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("id", "password", "last_login", "is_superuser", "username",
                  "first_name", "last_name", "email", "is_staff", "is_active",
                  "date_joined", "url", "gravatar", "activation_token",
                  "reset_password_token")
