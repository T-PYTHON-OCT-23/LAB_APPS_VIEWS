from django.urls import path
from . import views
app_name = "sales"
urlpatterns = [
    path("", views.index_view, name="index_view"),
    path("info/", views.info_view, name="info_view")
]