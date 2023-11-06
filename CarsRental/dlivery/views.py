from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def index_views(request:HttpRequest):
     return render(request,'dlivery/delivery.html')
    


