from django.shortcuts import render

from django.http import HttpRequest, HttpResponse


def view(request : HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here."
    return HttpRequest(content)

def viewPhrase(request : HttpRequest):
    content = "A car rental, hire car or car hire agency is a company that rents automobiles for short periods of time to the public, generally ranging from a few hours to a few weeks. It is often organized with numerous local branches (which allow a user to return a vehicle to a different location), and primarily located near airports or busy city areas and often complemented by a website allowing online reservations"
    return HttpRequest(content)
