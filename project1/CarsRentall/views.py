from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
def car_view(request:HttpRequest):
    return render(request, 'CarsRentall/about.html')

def car1_view(request : HttpRequest):
       return render(request, 'CarsRentall/home.html')
