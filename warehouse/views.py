from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Warehouse
from .serializer import WarehouseSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer