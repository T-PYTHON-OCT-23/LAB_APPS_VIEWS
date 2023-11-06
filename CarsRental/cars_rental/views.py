from django.shortcuts import render
from django.http import HttpRequest, HttpResponse 
# Create your views here.

def home(request : HttpRequest):
 content = "<h1>Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.</h1>"
 return HttpResponse (content)


def about (request : HttpRequest):
    content= "<p>Car rental agencies primarily serve people who require a temporary vehicle, for example, those who do not own their own car, travelers who are out of town, or owners of damaged or destroyed vehicles who are awaiting repair or insurance compensation. Car rental agencies may also serve the self-moving industry needs, by renting vans or trucks, and in certain markets, other types of vehicles such as motorcycles or scooters may also be offered.</p>"
    return HttpRequest (content)