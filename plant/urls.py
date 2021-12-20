from django.urls import path
from . import views
from .views import PredictView
urlpatterns = [
    path('', views.__index__function),
    path('predict', views.predict_plant_disease),
    path('predict_image', PredictView.as_view())
]
