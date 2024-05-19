from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authorization import views

urlpatterns = [
    path('register/', views.RegistrationView.as_view()),
    path('me/', views.UserCRUDView.as_view(), name="me"),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
