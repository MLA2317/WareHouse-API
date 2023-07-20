from django.contrib import admin
from .models import Product, ProductItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'zona', 'brand', 'product_name', 'prod_img', 'description')


@admin.register(ProductItem)
class ProductItem(admin.ModelAdmin):
    list_display = ('id', 'product_item', 'choice', 'quantity', 'price', 'created_date')
