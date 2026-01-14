from django.contrib import admin
from django.urls import path
from project_middleware.views import index

urlpatterns = [
    path('home/', index),
]