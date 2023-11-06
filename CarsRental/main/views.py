from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.
def car_home(request:HttpRequest):
    return render(request,"main/home.html")

def car_info(request:HttpRequest):
    return render(request,"main/about.html")