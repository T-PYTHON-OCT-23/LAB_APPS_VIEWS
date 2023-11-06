from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.

def get_info(request:HttpRequest):
    
    return render(request, "info/about.html")

def get_index(request:HttpRequest):
    
    
    return render(request, "info/index.html")