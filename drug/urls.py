from django.urls import path
from .views import (DrugView, FilterView, DrugByIdView,
                    PharmacyDrugView, DeleteDrugView)

urlpatterns = [

    path('add', DrugView.as_view()),
    path('update/<int:pk>', DrugView.as_view()),
    path('drug-id/<int:pk>', DrugByIdView.as_view()),
    path('delete/<int:drug_id>', DeleteDrugView.as_view()),
    path('pharmacy-drugs', DrugView.as_view()),
    path('pharmacy-drugs/<int:user_id>', PharmacyDrugView.as_view()),
    path('pharmacy-drugs/drug-name/<str:disease>', FilterView.as_view()),


]
