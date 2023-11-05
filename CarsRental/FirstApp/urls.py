from django.urls import path
from . import views
app_name = "FirstApp"

urlpatterns = [
    path("", views.page_view, name="page_view"),
    path("info/", views.page_info, name="page_info")
]
