from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.apps import UserConfig
from user.views import UserCreateAPIView

app_name = UserConfig.name

urlpatterns = [

    path('create/', UserCreateAPIView.as_view(), name='user_create'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
