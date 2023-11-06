
# Create your views here.
'''from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
def page_view(request : HttpRequest):
 content = "Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here."
 return HttpResponse(content)
def page2_view(request : HttpRequest):
 content = "A simple paragraph about Car Rentals."
 return HttpResponse(content)'''
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
#view in django
def index_view(request:HttpRequest):
    
    return render(request, 'main/home.html')

def about_view(request:HttpRequest):
    content = "<h1 style='color:magenta;'>A simple paragraph about Car Rentals </h1>   "
    return HttpResponse(content)