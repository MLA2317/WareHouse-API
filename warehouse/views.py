# from django.shortcuts import render
# from rest_framework import generics, viewsets, serializers
# from .models import Warehouse, Order, OrderItem
# from product.models import ProductItem
# from .serializer import WarehouseSerializer, OrderSerializer, OrderItemSerializer
#
#
# class WarehouseViewSet(viewsets.ModelViewSet):
#     queryset = Warehouse.objects.all()
#     serializer_class = WarehouseSerializer
# #
# # class WarehouseCreate(generics.CreateAPIView):
# #     queryset = Warehouse.objects.all()
# #     serializer_class = WarehousePostSerializer
# #
# #
# # class WareHouseList(generics.ListAPIView):
# #     queryset = Warehouse.objects.all()
# #     serializer_class = WareHouseGETSerializer
# #
#
#
# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#
# # class OrderItemViewSet(viewsets.ModelViewSet):
# #     queryset = OrderItem.objects.all()
# #     serializer_class = OrderItemSerializer
#
#
# class OrderItemViewSet(viewsets.ModelViewSet):
#     queryset = OrderItem.objects.all()
#     serializer_class = OrderItemSerializer
#
#     def perform_create(self, serializer):
#         product_item = self.request.data.get('product_item')
#         quantity = int(self.request.data.get('quantity', 0))
#
#         product_item_instance = ProductItem.objects.get(id=product_item)
#
#         # Check if enough stock is available
#         if product_item_instance.quantity < quantity:
#             raise serializers.ValidationError('Bu mahsulot qolamdi!')
#
#         # Deduct stock
#         product_item_instance.quantity -= quantity
#         product_item_instance.save()
#
#         # Call the serializer's create method
#         serializer.save()
