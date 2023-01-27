from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
from inventory_editor.models import Item
from django.core.serializers import serialize
import json
import inventory_editor.services as services
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    f = open('../html/index.html', 'r')
    return HttpResponse(f.read(), content_type="text/html")

def img(request):
    f = open('../html/img.jpg', 'rb')
    return HttpResponse(f.read(), content_type="image/jpeg")


def get_items(request):
    return JsonResponse(services.get_all_items(), safe=False)

@csrf_exempt
def add_item(request):
    services.add_new_item(request)
    response = HttpResponse("Added Item Successfully")
    response.status_code = 200
    return response

def get_items_search(request : HttpRequest):
    if(request.GET.get('name') != None):
        return JsonResponse(services.get_items_by_field("name", request.GET.get('name')), safe=False)
    if(request.GET.get('desc') != None):
        return JsonResponse(services.get_items_by_field("desc", request.GET.get('desc')), safe=False)


@csrf_exempt
def update_item(request : HttpRequest):
    services.update_item(request)
    response = HttpResponse("Updated Item Successfully")
    response.status_code = 200
    return response



