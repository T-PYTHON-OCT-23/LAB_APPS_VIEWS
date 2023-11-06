from django.shortcuts import render

from django.http import HttpRequest, HttpResponse


def view(request : HttpRequest):
    
    return render(request, 'CarRental/main.html')


def viewPhrase(request : HttpRequest):
    
    return render(request, 'CarRental/home.html')
