from django.shortcuts import render
from rest_framework import generics, viewsets, serializers, permissions, status
from .models import Warehouse, Cart, CartItem, Order
from rest_framework.response import Response
from product.models import ProductItem
from .serializer import WarehouseGETSerializer, WarehousePOSTSerializer, CartGETSerializer, CartPostSerializer, CartItemGETSerializer, CartItemPOSTSerializer, \
    OrderGETSerializer, OrderPostSerializer


class WarehouseListCreate(generics.ListCreateAPIView):
    queryset = Warehouse.objects.all()
    # serializer_class = WarehouseGETSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WarehousePOSTSerializer
        if self.request.method == 'GET':
            return WarehouseGETSerializer
        return Response({'detail': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class WarehouseRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseGETSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'pk'


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

