from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('test/', views.test, name='blog-test'),
]