from django.urls import path
from . import views

app_name = "dlivery"


urlpatterns = [
    path("delivery/", views.index_views, name="index_views")
]