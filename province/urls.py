from django.urls import path
from .views import ProvinceView

urlpatterns = [
    path("provinces", ProvinceView.as_view())
]
