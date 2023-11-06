from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
def home_view(request : HttpRequest):
    return render(request,'rental/home.html')
def car_rental_paragraph(request : HttpRequest):
    return render(request,'rental/info.html')
    