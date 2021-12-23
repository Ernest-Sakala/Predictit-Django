from django.urls import path
from .views import PharmacyDetailView
urlpatterns = [

    path("add", PharmacyDetailView.as_view())
]
