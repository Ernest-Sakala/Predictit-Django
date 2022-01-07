from django.urls import path
from .views import (DrugView, FilterView, DrugByIdView,
                    PharmacyDrugView, DeleteDrugView)

urlpatterns = [

    path('add', DrugView.as_view()),
    path('update', DrugView.as_view()),
    path('drug-id', DrugByIdView.as_view()),
    path('delete', DeleteDrugView.as_view()),
    path('pharmacy-drugs', DrugView.as_view()),
    path('drugs', PharmacyDrugView.as_view()),
    path('drugs/drug-name', FilterView.as_view()),


]
