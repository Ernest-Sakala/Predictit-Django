from django.urls import path
from .views import (OrderView, PharmacyOrderView)

urlpatterns = [
    path("add", OrderView.as_view()),
    path("orders", OrderView.as_view()),
    path("delete", OrderView.as_view()),
    path("pharmacy-orders", PharmacyOrderView.as_view())
]
