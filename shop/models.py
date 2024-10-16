from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50, default="", blank=True)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300, default="", blank=True)
    published_date = models.DateField()
    image = models.ImageField(upload_to='shop/images') # uploads into root media/shop/images
    # rating and reviews can also be added

    def __str__(self):
        return self.product_name
