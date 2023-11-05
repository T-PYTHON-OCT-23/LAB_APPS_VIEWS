from django.shortcuts import render
from django.http import HttpRequest, HttpResponse 
# Create your views here.

def home(request : HttpRequest):
 content = "<h1>Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.</h1>"
 return HttpResponse (content)
