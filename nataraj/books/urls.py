from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.index, name='index'),
]
