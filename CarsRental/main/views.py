from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.
def car_home(request:HttpRequest):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")

def car_info(request:HttpRequest):
    return HttpResponse("A simple paragraph about Car Rentals. ")