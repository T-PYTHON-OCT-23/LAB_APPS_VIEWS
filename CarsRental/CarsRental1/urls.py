from django.urls import path 
from . import views


app_name = "CarsRental"

urlpatterns = [
    path('' , views.index_car_view , name = "view_car"),
    path('info/' , views.index_car_view2 , name="view_car2")
]