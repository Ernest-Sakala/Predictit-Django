from django.urls import path
from .views import DiseaseView

urlpatterns = [
     path('diseases', DiseaseView.as_view())
   
]
