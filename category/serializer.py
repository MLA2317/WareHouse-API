from rest_framework import serializers
from .models import Blog, Category, Zona


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title')


class CategorySerializer(serializers.ModelSerializer):
    blog = BlogSerializer()

    class Meta:
        model = Category
        fields = ('id', 'blog', 'title', 'cat_img')


class ZonaSerializer(serializers.ModelSerializer):
    cat = CategorySerializer(read_only=True)

    class Meta:
        model = Zona
        fields = ('id', 'cat', 'choice', 'product')
