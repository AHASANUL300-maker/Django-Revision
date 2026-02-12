from django.shortcuts import render
from django.http import JsonResponse
from .models import Store

# Create your views here.

def index(request):
    data = {
        "status": True,
        "message": "Welcome to the Middleware Project"
    }
    return JsonResponse(data)

def contact(request):
    pass
    # print(request.headers)
    # store = Store.objects.get(bmp_id = (request.headers.get('bmp')))

    # data = {
    #     "status": True,
    #     "message": "store data",
    #     "data": {
    #         "bmp_id": store.bmp_id,
    #         "strore_name": store.strore_name
    #     }
    # }

    # return JsonResponse(data)

def about(request):
    pass


