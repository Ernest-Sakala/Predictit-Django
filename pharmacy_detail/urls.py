from django.urls import path
from .views import (PharmacyDetailView, PharmacyDetails)
urlpatterns = [

    path("add", PharmacyDetailView.as_view()),
    path("pharmacy-details", PharmacyDetailView.as_view()),
    path("details", PharmacyDetails.as_view())
]
