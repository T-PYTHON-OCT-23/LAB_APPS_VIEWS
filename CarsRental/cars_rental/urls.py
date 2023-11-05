from django.urls import path
from . import views

app_name = "cars_rental"

urlpatterns = [
    path("",views.index_view, name = "index_view"),
    path("info/", views.about_car_rentals , name ="about_car_rentals")
]