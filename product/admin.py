from django.contrib import admin
from .models import Product, ProductImage, ProductItem


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


admin.site.register(Product, ProductAdmin)


# class ProductItemAdmin(admin.ModelAdmin):
#     list_display = ('id', 'product_item', 'choice', 'quantity', 'price', 'created_date')


admin.site.register(ProductItem)


