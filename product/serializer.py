from rest_framework import serializers
from product.models import Product, ProductImage, ProductItem


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'product', 'prod_img')


class ProductGETSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'brand', 'description', 'images', 'choice', 'price')


class ProductPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'brand', 'description', 'images', 'choice', 'price')


class ProductItemGETSerializer(serializers.ModelSerializer):
    products = ProductGETSerializer(read_only=True)

    class Meta:
        model = ProductItem
        fields = ('id', 'products', 'choice', 'quantity', 'created_date')


class ProductItemPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = ('id', 'products', 'choice', 'quantity', 'created_date')

