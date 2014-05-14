from rest_framework import viewsets

from .models import Stack
from .serializers import StackSerializer


class StackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Stack model to be viewed or edited.
    """
    queryset = Stack.objects.all()
    serializer_class = StackSerializer
