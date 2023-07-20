from rest_framework import serializers
from .models import Product, ProductItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'zona', 'brand', 'product_name', 'prod_img', 'description')


class ProductItemSerializer(serializers.ModelSerializer):
    #product_items = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = ProductItem
        fields = ('id', 'product_item', 'choice', 'quantity', 'price', 'created_date')
