from django.urls import path
from . import views

app_name = "CarsRentall"

urlpatterns = [
    path('',views.car_view,name="cars"),
    path('info/',views.car1_view,name ='info')
]