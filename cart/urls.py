from .views import CartView
from django.urls import path


urlpatterns = [
    path('add', CartView.as_view()),
    path('update', CartView.as_view()),
    path('items', CartView.as_view()),
    path('delete', CartView.as_view())
]
