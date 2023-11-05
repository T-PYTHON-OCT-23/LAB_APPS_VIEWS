from django.urls import path
from . import views

cars_rental="cars_rental"

urlpatterns = [
    path("",views.home, name="home"),

]