from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.CarsRental_home_view, name="CarsRental_home_view"),
    path("about/", views.paragraph_about_view, name="paragraph_about_view")

]


