from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
def home_view(request : HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! were excited to welcome you here."
    return HttpResponse(content)
def car_rental_paragraph(request : HttpRequest):
    content = "Car rentals allow people to access a vehicle without having to purchase one. This can be convenient for a variety of reasons, such as traveling, moving, or simply needing a car for a short period of time."
    return HttpResponse(content)