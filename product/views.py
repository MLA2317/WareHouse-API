from django.shortcuts import render
from rest_framework import generics, status, permissions, views
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from product.models import Product, ProductImage, ProductItem
from .serializer import ProductGETSerializer, ProductPOSTSerializer, ProductItemGETSerializer, ProductItemPOSTSerializer


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


class ProductItemList(generics.ListAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemGETSerializer
    permissions = [permissions.IsAdminUser]


class ProductItemCreate(generics.CreateAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemPOSTSerializer
    permission_classes = [permissions.IsAdminUser]


class ProductItemRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemGETSerializer
    permissions = [permissions.IsAdminUser]
#
#
# class ProductItemRUD(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ProductItem.objects.all()
#     serializer_class = ProductItemSerializer
#     permissions = [permissions.IsAdminUser]

    # def put(self, request, *args, **kwargs):
    #     try:
    #         instance = self.get_object()
    #         serializer = ProductItemSerializer(instance, data=request.data)
    #         print('ser', serializer)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         print('save', serializer.save())
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except ValidationError as e:
    #         return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
