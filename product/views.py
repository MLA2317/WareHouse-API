from django.shortcuts import render
from rest_framework import generics, status, permissions, views
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from product.models import Product, ProductImage
from .serializer import ProductGETSerializer, ProductPOSTSerializer, ProductImageSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductGETSerializer
    permissions = [permissions.IsAdminUser]


class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductPOSTSerializer
    permission_classes = [permissions.IsAdminUser]


class ProductRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductGETSerializer
    permissions = [permissions.IsAdminUser]


class ProductImageList(generics.ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = permissions.IsAuthenticated
