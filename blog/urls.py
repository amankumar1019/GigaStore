from tkinter.font import names

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blog_index"),
    path('', views.google, name="blog_google"),
]
