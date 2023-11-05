from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def index_views(request:HttpRequest):
    return HttpResponse(" <h1>Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.<h1>")

def next_views(request:HttpRequest):
    return HttpResponse(" <h1>A simple paragraph about Car Rentals. <h1>")
