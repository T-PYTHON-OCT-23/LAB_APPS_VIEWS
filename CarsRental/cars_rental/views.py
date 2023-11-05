from django.shortcuts import render
from django.http import HttpRequest , HttpResponse

# Create your views here.

def index_view(request:HttpRequest):
    text = "<h1 style='color:magenta;'>Hello World, </h1> \n This is my new HOME for Car Rentals Website ! we're excited to welcome you here. "
    return HttpResponse(text)

def about_car_rentals(request:HttpRequest):
    text = "<h1 style='color:blue;'> A simple paragraph about Car Rentals. </h1> <h3> \n We have great offers for daily, weekly and long term rentals. Find the cheapest prices online, for your future Car Rental in 4 quick easy steps. Book now at the lowest possible rates only with a small down payment and pay the rest when you pick up the car. </h3>"
    return HttpResponse(text)
