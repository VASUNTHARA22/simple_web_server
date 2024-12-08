from django.urls import path
from . import views

urlpatterns = [
    path('', views.laptop_details, name='laptop_details'),
]
