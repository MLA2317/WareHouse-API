from django.shortcuts import render
from rest_framework import generics, status, permissions
from .models import Product, ProductItem
from .serializer import ProductSerializer, ProductItemSerializer


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permissions = [permissions.IsAuthenticated]


class ProductItemListCreate(generics.ListCreateAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
    permissions = [permissions.IsAuthenticated]