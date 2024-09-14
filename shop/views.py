from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .models import Product


# Create your views here.
def index(request):
    return render(request,"shop/index.html")
    # return HttpResponse("Success")

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("contact")

def track_order(request):
    return HttpResponse("track order")

def product_view(request):
    # productView
    from .models import Product
    object_list = Product.objects.all().values()
    return render(request, 'shop/product.html', {'object_list':object_list})

def search(request):
    return HttpResponse("search")

def checkout(request):
    return HttpResponse("checkout")