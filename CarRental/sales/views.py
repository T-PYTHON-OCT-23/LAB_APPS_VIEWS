from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index_view(request:HttpRequest):
    return render(request,'sales/salesPage.html')

def info_view(request:HttpRequest):
       return render(request,'sales/salesInfo.html')