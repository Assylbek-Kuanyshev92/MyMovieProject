from rest_framework.response import Response

from authorization.models import User
from authorization.serializers import RegistrationSerializer, UserSerializer
from rest_framework import generics, status
from rest_framework import permissions
from django.contrib.auth.hashers import make_password
import requests


# registration
class UserCRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


# registration
class RegistrationView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        # Получение координат из API
        response = requests.get('http://ip-api.com/json/')
        data = response.json()
        latitude = data.get('lat')
        longitude = data.get('lon')
        request.data['latitude'] = latitude
        request.data['longitude'] = longitude
        request.data['password'] = make_password(request.data['password'])
        print(request.data['latitude'], request.data['longitude'])
        return super().create(request, *args, **kwargs)