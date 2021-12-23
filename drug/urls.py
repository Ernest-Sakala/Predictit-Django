from django.urls import path
from .views import (DrugView, FilterView)

urlpatterns = [

    path('add', DrugView.as_view()),
    path('pharmacy-drugs/<int:pk>', DrugView.as_view()),
    path('pharmacy-drugs', DrugView.as_view()),
    path('pharmacy-drugs/<int:user_id>', DrugView.as_view()),
    path('pharmacy-drugs/drug-name/<str:disease>', FilterView.as_view()),


]
