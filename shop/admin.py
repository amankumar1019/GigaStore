
from django.contrib import admin

# Register your models here.

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fields = [
                "product_name",
                "description",
                "category",
                "subcategory",
                "price",
                "published_date",
                "image"
    ]

admin.site.register(Product, ProductAdmin)
