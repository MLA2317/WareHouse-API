from rest_framework import serializers
from product.models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'product', 'prod_img')


class ProductGETSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'brand', 'description', 'images', 'choice', 'price', 'category_id', 'quantity', 'created_date')


class ProductPOSTSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'brand', 'description', 'images', 'choice', 'price', 'category_id', 'quantity',)

