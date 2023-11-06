from django.shortcuts import render
from django.http import HttpRequest , HttpResponse


# Create your views here.
def index_car_view(request: HttpRequest):
    return render(request, 'main/index_car_view.html')


# Create your views here.
def index_car_view2(request: HttpRequest):
    return render(request, 'main/index_car_view2.html')
