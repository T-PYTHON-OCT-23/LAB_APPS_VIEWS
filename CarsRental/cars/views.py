from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def index(request:HttpRequest):
    
    return render(request,'cars/index.html')

def info(request:HttpRequest):
    
    return render(request,'cars/info.html')