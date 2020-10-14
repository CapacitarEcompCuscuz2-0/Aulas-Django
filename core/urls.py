from django.urls import path
from . import views

urlpatterns = [
    path('inicio/<int:numero>/', views.index),
]