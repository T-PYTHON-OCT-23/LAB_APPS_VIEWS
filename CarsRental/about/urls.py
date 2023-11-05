from django.urls import path
from . import views

about= "about"
urlpatterns =[
    path("",views.about, name="about"),
]