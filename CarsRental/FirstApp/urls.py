from django.urls import path
from django.urls import include
from . import views
app_name = "FirstApp"

urlpatterns = [
    path("", views.page_view, name="page_view")
]
