from django.shortcuts import render
from django.http import HttpRequest , HttpResponse

# Create your views here.

def index_view(request:HttpRequest):
    
    return render(request ,'cars_rental/index_cars_rental.html' )

def about_car_rentals(request:HttpRequest):
    
    return render(request , 'cars_rental/about_car_rentals.html')
