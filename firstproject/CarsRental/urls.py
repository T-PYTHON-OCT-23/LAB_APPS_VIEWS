from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
    path("home/", views.start_delivery_view, name="home"),
    path("", views.index_view, name="index_view"),
    path("info/", views.about_view, name="about_view")
]