from rest_framework import serializers
from .models import Blog, Category, Zona


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title', 'cat_img')


class ZonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zona
        fields = ('id', 'zona', 'product')
