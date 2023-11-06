from django.urls import path
from . import views

app_name = "cars"
urlpatterns = [path("path/to/view/", views.page_view, name="CarRentals"),]
