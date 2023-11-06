from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def page_view(request : HttpRequest):

    return render(request,'FirstApp/home.html')



# Create your views here.
