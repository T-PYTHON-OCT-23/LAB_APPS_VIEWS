from django.urls import path
from . import views
app_name = "rental"
urlpatterns = [path("", views.home_view, name="home_page"),
               path('info/',views.car_rental_paragraph,name='car_rental_paragraph')
               ]