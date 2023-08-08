from django.shortcuts import render
from rest_framework import generics, status, permissions
from .models import Category
from .serializer import CategorySerializer


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission = [permissions.IsAdminUser]
