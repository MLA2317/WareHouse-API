from django.shortcuts import render
from rest_framework import generics, viewsets, serializers, permissions, status
from .models import Warehouse, Order, OrderProduct, Leaving, Location
from rest_framework.response import Response
from product.models import Product
from .serializer import WarehouseGetSerializer, WarehousePostSerializer, LocationSerializer, OrderGetSerializer,\
    OrderPostSerializer, OrderProductGetSerializer, OrderProductPostSerializer, LeavingGetSerializer, LeavingPostSerializer


class LocationListCreate(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]


class WarehouseList(generics.ListAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseGetSerializer
    permission_classes = [permissions.IsAuthenticated]


class WarehouseCreate(generics.CreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehousePostSerializer
    permission_classes = [permissions.IsAuthenticated]


class WarehouseRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehousePostSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'pk'

class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderGetSerializer
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


class OrderProdCreate(generics.CreateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductPostSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderProdList(generics.ListAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductGetSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderProdRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderProductPostSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]


class LeavingList(generics.ListAPIView):
    queryset = Leaving.objects.all()
    serializer_class = LeavingGetSerializer
    permission_classes = [permissions.IsAuthenticated]


class LeavingCreate(generics.CreateAPIView):
    queryset = Leaving.objects.all()
    serializer_class = LeavingPostSerializer
    permission_classes = [permissions.IsAuthenticated]


class LeavingRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Leaving.objects.all()
    serializer_class = LeavingPostSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]

