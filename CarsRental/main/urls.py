from django.urls import path
from . import views

app_name = "main"

urlpatterns =[
    path("", views.car_home, name="car_home"),
    path("info/" , views.car_info , name="car_info")
]