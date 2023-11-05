from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def index_view(request:HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here."
    return HttpResponse(content)


def about(request:HttpRequest):
    content = "<p style='color:magenta;'>Car rental is when you rent a car. The company providing you the car becomes the car rental service provider, whereas you become the car hirer, as you hire the car for a fee. </p>   "
    return HttpResponse(content)