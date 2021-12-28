from django.urls import path
from .views import TownView

urlpatterns = [
    path("towns", TownView.as_view())
]
