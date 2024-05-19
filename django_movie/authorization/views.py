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
        try:
            # Получение координат из API
            response = requests.get('http://ip-api.com/json/')
            response.raise_for_status()
            data = response.json()
            latitude = data.get('lat')
            longitude = data.get('lon')
        except requests.RequestException as e:
            return Response({'error': 'Unable to fetch coordinates'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        data = request.data.copy()
        request.data['latitude'] = latitude
        request.data['longitude'] = longitude

        if 'password' in data:
            data['password'] = make_password(data['password'])

        print(request.data['latitude'], request.data['longitude'])
        return super().create(request, *args, **kwargs)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
