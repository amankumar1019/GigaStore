from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .models import Product


# Create your views here.
def index(request):
    return render(request,"shop/index.html")
    # return HttpResponse("Success")

def about(request):
    return HttpResponse("about")

def contact(request):
    return HttpResponse("contact")

def track_order(request):
    return HttpResponse("track order")

def product_view(request):
    # productView
    obj = models.Product
    from .models import Product
    def productlist(request):
        context = {
            'product': Product.objects.all()
        }
        return render(request, 'shop/product.html', context)
    return render(request, 'product.html', )

def search(request):
    return HttpResponse("search")

def checkout(request):
    return HttpResponse("checkout")