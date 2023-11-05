from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.

def get_info(requet:HttpRequest):
    body = '''Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here.'''
    return HttpResponse(body)

def get_index(request:HttpRequest):
    body = '''<h1>Car rental agencies primarily serve people who require a temporary vehicle</h1>,<h3> for example, those who do not own their own car, travelers who are out of town, or owners of damaged or destroyed vehicles who are awaiting repair or insurance compensation.</h3>'''

    return HttpResponse(body)