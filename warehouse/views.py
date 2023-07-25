from django.shortcuts import render
from rest_framework import generics, viewsets, serializers
from .models import Warehouse, Cart, CartItem, Order
from product.models import ProductItem
from .serializer import WarehouseSerializer, CartGETSerializer, CartPostSerializer, CartItemGETSerializer, CartItemPOSTSerializer, \
    OrderGETSerializer, OrderPostSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class CartList(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartGETSerializer


class CartCreate(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartPostSerializer


class CartRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartPostSerializer
    lookup_field = 'pk'


class CartItemList(generics.ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemGETSerializer


class CartItemCreate(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemPOSTSerializer


class CartItemRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemPOSTSerializer
    lookup_field = 'pk'


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderGETSerializer


class OrderCreate(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderPostSerializer


class OrderRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderPostSerializer
    lookup_field = 'pk'

