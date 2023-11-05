from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('',views.index,name="cars"),
    path('info/',views.info,name ='info')
]