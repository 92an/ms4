from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.artwork, name="artwork"),
    path("<artwork_id>", views.artwork_detail, name="artwork_detail"),
]
