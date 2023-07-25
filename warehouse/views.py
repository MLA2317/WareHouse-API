from django.shortcuts import render
from rest_framework import generics, viewsets, serializers, permissions
from .models import Warehouse, Cart, CartItem, Order
from product.models import ProductItem
from .serializer import WarehouseSerializer, CartGETSerializer, CartPostSerializer, CartItemGETSerializer, CartItemPOSTSerializer, \
    OrderGETSerializer, OrderPostSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [permissions.IsAuthenticated]


class CartList(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartGETSerializer
    permission_classes = [permissions.IsAuthenticated]


class CartCreate(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartPostSerializer
    permission_classes = [permissions.IsAuthenticated]


class CartRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartPostSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]


class CartItemList(generics.ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemGETSerializer
    permission_classes = [permissions.IsAuthenticated]


class CartItemCreate(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemPOSTSerializer
    permission_classes = [permissions.IsAuthenticated]


class CartItemRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemPOSTSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderGETSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderCreate(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderPostSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderPostSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]

