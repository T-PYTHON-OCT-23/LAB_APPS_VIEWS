from django.urls import path
from . import views
app_name = "sales"
urlpatterns = [
    path("sales/home/", views.index_view, name="home_page"),
    path("sales/info/", views.info_view, name="info_view")
]