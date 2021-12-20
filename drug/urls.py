from django.urls import path
from .views import DrugView


urlpatterns = [

    path('add', DrugView.as_view()),
    path('pharmacy-drugs/<int:pk>', DrugView.as_view()),

]
