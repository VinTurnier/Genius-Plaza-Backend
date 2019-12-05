# Rest Framework Application Imports
from rest_framework.response import Response 
from rest_framework import generics

# Django Application Imports
from django.contrib.auth import get_user_model

# Local Application Imports
from user.serializers import UserSerializer, SingleUserSerializer

class UserViewSet(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserSingleViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = SingleUserSerializer

