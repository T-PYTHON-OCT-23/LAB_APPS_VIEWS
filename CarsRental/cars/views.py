from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.

def index(request:HttpRequest):
    content ='<h1>Hello World, This is my new HOME for Car Rentals Website  ! we are excited to welcome you here.</h1>'
    return HttpResponse(content)

def info(request:HttpRequest):
    content = '<h1>A simple paragraph about Car Rentals.</h1>'
    return HttpResponse(content)