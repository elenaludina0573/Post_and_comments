from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from users.apps import UsersConfig

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.permissions import IsOwner
from users.views import UserCreateAPIView, UserUpdateAPIView, UserRetrieveAPIView, UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = ([
    path('register/', UserCreateAPIView.as_view(permission_classes=(AllowAny, )), name='register'),
    path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny, )), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny, )), name='token_refresh'),
    path('update/', UserUpdateAPIView.as_view(permission_classes=(IsAdminUser, IsOwner)), name='update'),
    path('retrieve/', UserRetrieveAPIView.as_view(permission_classes=(IsAdminUser, IsAuthenticated)), name='retrieve'),
    path('delete/', UserDestroyAPIView.as_view(permission_classes=(IsAdminUser, )), name='delete')
])

