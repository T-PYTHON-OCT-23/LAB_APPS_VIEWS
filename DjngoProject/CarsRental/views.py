from django.shortcuts import render
from django.http import HttpRequest , HttpResponse


# Create your views here.
def index_car_view(request: HttpRequest):
    phrase="Hello World, This is my new HOME for Car Rentals Website! we're excited to welcome you here."
    return HttpResponse(phrase)

# Create your views here.
def index_car_view2(request: HttpRequest):
    phrase="<p style= 'color:white;  background-color: black;'>Car rentals are very popular today which means that rental agencies are all looking for ways to get your custom. To do this they are offering highly competitive prices and all good agencies will have a wide choice of cars. A good agency will recognize that everyone has their own car of preference and should try to provide cars that fit the needs of their customers.</p>"
    return HttpResponse(phrase)
