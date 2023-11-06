from django.urls import path
from . import views

Cars = "CARS"
urlpatterns = [
    path("path/to/view/", views.page_view, name="page_view"),
]
