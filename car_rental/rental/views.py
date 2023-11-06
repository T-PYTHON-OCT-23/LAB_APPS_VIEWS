from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request,'main/main.html')


def info(request):
    
    return render(request,'main/info.html')
