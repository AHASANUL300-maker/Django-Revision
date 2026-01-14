from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    data = {
        "status": True,
        "message": "Welcome to the Middleware Project"
    }
    return JsonResponse(data)

def contact(request):
    pass


