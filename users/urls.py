from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from .views import RegisterAPIView, UserListAPIView, UserDetailAPIView, ProfilUpdateAPIView



urlpatterns = [
    # JWT tokenlar
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Ro'yxatdan o'tish
    path('register/', RegisterAPIView.as_view(), name='register'),

    # user list, detail
    path('list/',UserListAPIView.as_view()),
    path('detail/',UserDetailAPIView.as_view()),

   

]
