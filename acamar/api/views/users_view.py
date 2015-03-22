from django.contrib.auth.models import User
from rest_framework import viewsets
from api import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_fields = ('username',)
