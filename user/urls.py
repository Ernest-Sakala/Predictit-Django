from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import CustomUserCreate, MyTokenObtainPairView

urlpatterns = [

    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', CustomUserCreate.as_view()),
    path('details', CustomUserCreate.as_view()),
    path('login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('pharmacies', CustomUserCreate.as_view())

]
