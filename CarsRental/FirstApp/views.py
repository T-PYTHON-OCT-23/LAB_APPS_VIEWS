from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def page_view(request : HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here."
    return HttpResponse(content)

def page_info(request : HttpRequest):
    content = "Car rental is a service that allows people to rent a car for a short period of time. It is a popular option for people who are traveling, need a car for a special occasion, or whose car is in the shop. Car rental companies offer a wide variety of cars to choose from, including sedans, SUVs, minivans, and trucks."
    return HttpResponse(content)


# Create your views here.
