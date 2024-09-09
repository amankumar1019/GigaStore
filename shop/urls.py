from tkinter.font import names

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="shop_index"),
    path("about", views.about, name="shop_about"),
    path("contact", views.contact, name="shop_contact"),
    path("trackOrder", views.track_order, name="shop_track_order"),
    path("productView", views.product_view, name="shop_product_view"),
    path("search", views.search, name="shop_search"),
    path("checkout", views.checkout, name="shop_checkout"),
]
