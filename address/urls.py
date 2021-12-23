from django.urls import path
from .views import AddressView

urlpatterns = [
    path('add', AddressView.as_view()),
    path('addresses/<int:pk>', AddressView.as_view())
]
