from rest_framework import serializers

from .models import Stack


# Django models
class StackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stack
        fields = ("id", "name", "description", "private", "sharelink",
                  "owner", "collaborators")  #"instance_set")
