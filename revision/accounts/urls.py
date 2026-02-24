from django.urls import path
from accounts.views import index, login, check_otp, dashboard

urlpatterns = [
    path('something/', index),
    path('check-otp/<int:user_id>/', check_otp),
    path('login/', login),
    path('dashboard/', dashboard)
]