from .views import CartView
from django.urls import path


urlpatterns = [
    path('add', CartView.as_view()),
    path('update/<int:pk>', CartView.as_view()),
    path('items/<int:pk>', CartView.as_view()),
    path('delete/<int:pk>', CartView.as_view())
]
