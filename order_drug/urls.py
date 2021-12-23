from django.urls import path
from .views import OrderDrugView
urlpatterns = [

    path("add", OrderDrugView.as_view())
]
