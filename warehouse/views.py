# from django.shortcuts import render
# from rest_framework import generics, viewsets, serializers, permissions, status
# from .models import Warehouse, Order, OrderProduct, Leaving, Location
# from rest_framework.response import Response
# from product.models import Product
# from .serializer import WarehouseSerializer, OrderSerializer, OrderProductSerializer, LocationSerializer, \
#     LeavingGetSerializer, LeavingPostSerializer
#
#
# class LocationListCreate(generics.ListCreateAPIView):
#     queryset = Location.objects.all()
#     serializer_class = LocationSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class WarehouseListCreate(generics.ListCreateAPIView):
#     queryset = Warehouse.objects.all()
#     # serializer_class = WarehouseGETSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class WarehouseRUD(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Warehouse.objects.all()
#     serializer_class = WarehouseSerializer
#     permission_classes = [permissions.IsAdminUser]
#     lookup_field = 'pk'
#
#
#
# class OrderListCreate(generics.CreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class OrderRUD(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     lookup_field = 'pk'
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class OrderProdCreateList(generics.ListCreateAPIView):
#     queryset = OrderProduct.objects.all()
#     serializer_class = OrderProductSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class OrderProdRUD(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     lookup_field = 'pk'
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class CartItemRUD(generics.RetrieveUpdateDestroyAPIView):
#     queryset = OrderProduct.objects.all()
#     serializer_class = OrderProductSerializer
#     lookup_field = 'pk'
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class LeavingList(generics.ListAPIView):
#     queryset = Leaving.objects.all()
#     serializer_class = LeavingGetSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class LeavingCreate(generics.CreateAPIView):
#     queryset = Leaving.objects.all()
#     serializer_class = LeavingPostSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class LeavingRUD(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Leaving.objects.all()
#     serializer_class = LeavingPostSerializer
#     lookup_field = 'pk'
#     permission_classes = [permissions.IsAuthenticated]
#
