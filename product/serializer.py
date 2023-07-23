from rest_framework import serializers
from product.models import Product, ProductItem
from category.serializer import ZonaSerializer


class ProductSerializer(serializers.ModelSerializer):
    zona = ZonaSerializer()

    class Meta:
        model = Product
        fields = ('id', 'zona', 'brand', 'product_name', 'prod_img', 'description')


class ProductItemSerializer(serializers.ModelSerializer):
    product_item = ProductSerializer()

    class Meta:
        model = ProductItem
        fields = ('id', 'product_item', 'choice', 'quantity', 'price', 'created_date')

