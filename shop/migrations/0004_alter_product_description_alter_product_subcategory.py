# Generated by Django 5.1 on 2024-09-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_category_alter_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
