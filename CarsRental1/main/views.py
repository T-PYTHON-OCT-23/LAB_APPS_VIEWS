from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def CarsRental_home_view(request : HttpRequest):
   
   return render(request,"main/home.html")

def paragraph_about_view(request : HttpRequest):
    
    return render(request,"main/about.html")
