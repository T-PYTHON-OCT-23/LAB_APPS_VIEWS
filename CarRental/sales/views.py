from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index_view(request:HttpRequest):
    content = """Hello World, This is my new HOME for Car Rentals Website! 
            We're excited to welcome you here."""
    return HttpResponse(content)

def info_view(request:HttpRequest):
    content = """Car rentals provide a convenient and flexible transportation solution for individuals and travelers. 
    Whether for business trips or leisure travel, car rental services offer a wide range of vehicles to choose from, allowing customers to select the most suitable option for their needs. 
    These services often include daily, weekly, or monthly rental options, making it easy for people to access a vehicle without the long-term commitment of ownership. 
    Car rentals are available at airports, city centers, and other convenient locations, making it easy to pick up and drop off vehicles. 
    This flexibility has made car rentals a popular choice for those looking for temporary transportation solutions."""
    return HttpResponse(content)