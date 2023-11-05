from django.urls import path
from . import views


app_name = "info"


urlpatterns = [
    path("info/", views.get_info, name="info"),
    path("" , views.get_index, name="index" )
]