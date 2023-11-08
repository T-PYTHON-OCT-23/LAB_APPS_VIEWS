from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
def page_view(request : HttpRequest):
 return render(request, 'main/index.html')

def info(request : HttpRequest):
 return render(request, 'main/info.html')
