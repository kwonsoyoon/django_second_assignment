from django.urls import path
from .views import home

urrlpattern = [
    path("", home)
]