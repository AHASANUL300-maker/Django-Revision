from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .emailer import sendOtpToEmail
import random
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

User = get_user_model()

def index(request):
    pass

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        user_obj = User.objects.filter(email = email)
        if not user_obj.exists():
            return redirect('/')
        
        otp = random.randint(1000, 9999)
        user_obj.update(otp=otp)
        subject = "OTP For Login"
        message = f"This is Your OTP {otp}"

        sendOtpToEmail(
            email, subject, message
        )
        print(user_obj)
        
        return redirect(f'/account/check-otp/{user_obj[0].id}/')

    return render(request, 'accounts/login.html')

def check_otp(request, user_id):
    if request.method=="POST":
        otp = request.POST.get('otp')
        user_obj = User.objects.get(id = user_id)
        if int(otp) == user_obj.otp:
            return redirect('/account/dashboard/')
        else:
            messages.error(request, "Wrong OTP.")
            return redirect(f'/account/check-otp/{user_obj.id}/')
    
    return render(request, 'accounts/check_otp.html')

def dashboard(request):
    return HttpResponse("You Logged in successfully with your OTP!")
