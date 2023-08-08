# from rest_framework import serializers
# from django.core.mail import send_mail
# from .models import Warehouse, Order, OrderProduct, Leaving, Location
# from product.serializer import ProductGETSerializer
#
#
# class LocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Location
#         fields = ('id', 'title')
#
#
# class WarehouseSerializer(serializers.ModelSerializer):
#     products = ProductGETSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Warehouse
#         fields = ('id', 'user', 'products', 'phone_number', 'email', 'location', 'enter_date')
#
#
# class OrderSerializer(serializers.ModelSerializer):
#     warehouse_id = WarehouseSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Order
#         fields = ('id', 'warehouse_id', 'customer_id', 'status')
#
#
# class OrderProductSerializer(serializers.ModelSerializer):
#     order_id = OrderSerializer(many=True, read_only=True)
#     quantity = serializers.CharField(max_length=100)
#
#     class Meta:
#         model = OrderProduct
#         fields = ('id', 'order_id', 'products', 'quantity')
#
#
# class LeavingGetSerializer(serializers.ModelSerializer):
#     order_prod_id = OrderProductSerializer(read_only=True)
#
#     class Meta:
#         model = Leaving
#         fields = ('id', 'order_prod_id', 'day_out')
#
#
# class LeavingPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Leaving
#         fields = ('id', 'order_prod_id', 'day_out')