from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


#view in django

def start_delivery_view(request : HttpRequest):

    return render(request,'CarsRental/home.html')

def index_view(request:HttpRequest):
    content = "<h3 style='color:pink;'>This is my new HOME for Car Rentals Website ! we're excited to welcome you here. </h3>"
    return HttpResponse(content)

def about_view(request:HttpRequest):
    content = "You must have a valid ID and passport ,The rental period should not be less than one day (24 hours)."  
    return HttpResponse(content)


