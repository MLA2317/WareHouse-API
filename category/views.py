from django.shortcuts import render
from rest_framework import generics, status, permissions
from .models import Blog, Category, Zona
from .serializer import BlogSerializer, CategorySerializer, ZonaSerializer


class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permissions = [permissions.IsAuthenticated]


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permissions = [permissions.IsAuthenticated]


class ZonaListCreate(generics.ListCreateAPIView):
    queryset = Zona.objects.all()
    serializer_class = ZonaSerializer
    permissions = [permissions.IsAuthenticated]