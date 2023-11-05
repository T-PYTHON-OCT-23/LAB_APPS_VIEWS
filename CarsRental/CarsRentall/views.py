from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
def car_view(request:HttpRequest):
    content = """Hello World, This is my new HOME for Car Rentals Website! 
            We're excited to welcome you here."""
    return HttpResponse(content)

def car1_view(request : HttpRequest):
    content = "Car rental companies offer a variety of cars to choose from,"
    return HttpRequest(content)
