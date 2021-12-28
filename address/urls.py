from django.urls import path
from .views import AddressView

urlpatterns = [
    path('add', AddressView.as_view()),
    path('update', AddressView.as_view()),
    path('addresses', AddressView.as_view()),
    path('delete', AddressView.as_view())
]
