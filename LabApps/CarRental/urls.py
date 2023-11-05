from django.urls import path
from . import views

app_name = "CarRental"

urlpatterns = [
    
    path("", views.view, name="view"),
    path("info/", views.viewPhrase, name="viewPhrase"),
]
