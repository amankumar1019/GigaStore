from unicodedata import category

from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from .models import Product


# Create your views here.
def index(request):
    products_by_category = {}
    categories = Product.objects.values_list('category', flat=True).distinct()
    for category in categories:
        products_by_category[category] = list(Product.objects.filter(category=category))
    products = Product.objects.all()
    params = {
        'products_by_category': products_by_category,
        'products':products
    }
    return render(request,"shop/index.html", params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def track_order(request):
    return render(request, 'shop/tracker.html')

def product_view(request, id):
    # productView
    # from .models import Product
    # object_list = Product.objects.all().values()
    selected_product = Product.objects.filter(id=id)
    params={
        'product': selected_product[0]
    }
    return render(request, 'shop/product.html', params)

def search(request):
    return render(request, 'shop/search.html')

def checkout(request):
    return render(request, 'shop/checkout.html')