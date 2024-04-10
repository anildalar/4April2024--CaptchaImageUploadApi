# imageapi/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('getBalance/',views.getBalance , name='getBalance'),
    path('getBalance', views.getBalance, name='getBalance'),
    path('createTask', views.createTask, name='createTask'),
    path('createTask/', views.createTask, name='createTask'),
]

#https://api.capsolver.com/createTask