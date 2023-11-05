from django.shortcuts import render
from django.http import HttpRequest , HttpResponse


# Create your views here.
def index_car_view(request: HttpRequest):
    phrase="Hello World, This is my new HOME for Car Rentals Website! we're excited to welcome you here."
    return HttpResponse(phrase)

# Create your views here.
def index_car_view2(request: HttpRequest):
    phrase="car rental is a helpful service that help people to find a car to use it in short peried of time"
    return HttpResponse(phrase)
