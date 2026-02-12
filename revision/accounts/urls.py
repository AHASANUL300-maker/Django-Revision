from django.contrib import admin
from django.urls import path
from accounts.views import index

urlpatterns = [
    path('something/', index),
]