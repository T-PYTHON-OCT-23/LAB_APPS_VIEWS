from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def CarsRental_home_view(request : HttpRequest):
   
   content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here"
   return HttpResponse(content)

def paragraph_about_view(request : HttpRequest):
    content=''' 
             Car rentals offer individuals the convenience of temporarily using a vehicle without the
             long-term commitment and responsibilities of ownership. Whether for leisure or business purposes,
             car rental services provide a wide range of vehicles to choose from, catering to various needs
             and preferences. Customers can rent cars for short or extended periods, making it a flexible
             transportation solution for travel, daily commuting, or special occasions. Car rentals often come
             with added benefits such as insurance coverage and maintenance, making them a popular choice for
             those looking for mobility and flexibility without the hassles of owning a car.
            '''
    return HttpResponse(content)
