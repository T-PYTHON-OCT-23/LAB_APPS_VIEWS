from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
    path("", views.index_views, name="index_views"),
    path("info/", views.next_views, name="next_views")
]