from rest_framework import serializers
from django.core.mail import send_mail
from .models import Warehouse, Order, OrderItem
from product.serializer import ProductSerializer, ProductItemSerializer
from category.serializer import BlogSerializer, CategorySerializer, ZonaSerializer


class WarehouseSerializer(serializers.ModelSerializer):
    # blog = BlogSerializer(read_only=True)
    # cat = CategorySerializer(read_only=True)
    # zon = ZonaSerializer(read_only=True)
    prod = ProductItemSerializer(read_only=True)

    class Meta:
        model = Warehouse
        fields = ('id', 'user', 'prod', 'phone_number', 'email', 'enter_date')

    # def create(self, validated_data):
    #     warehouse = super().create(validated_data)
    #     self.send_notification(warehouse)
    #     return warehouse
    #
    # def send_notification(self, Warehouse):
    #     send_mail(
    #         'Warehouse Company!',
    #         f'Sizning Mahsulotingiz omborxonada joylandi. Mahsulot Nomi: {Warehouse.prod.product_name}.',
    #         'omborxona@gmail.com',
    #         [Warehouse.email],
    #         fail_silently=False,
    #     )
#
#
# class WareHouseGETSerializer(serializers.ModelSerializer):
#     blog = BlogSerializer(read_only=True)
#     cat = CategorySerializer(read_only=True)
#     zon = ZonaSerializer(read_only=True)
#     prod = ProductSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Warehouse
#         fields = ('id', 'user','blog', 'cat', 'zon', 'prod', 'phone_number', 'email', 'enter_date')


class OrderSerializer(serializers.ModelSerializer):
    warehouse = WarehouseSerializer(read_only=True)
    # print('wa', ware)

    class Meta:
        model = Order
        fields = ('id', 'warehouse', 'user', 'phone_number', 'email')


class OrderItemGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product_item', 'choice', 'quantity', 'day_out')


# class OrderItemSerializer(serializers.ModelSerializer):
#     # product_item = ProductItemSerializer(read_only=True)
#     order = OrderSerializer(read_only=True)
#
#     class Meta:
#         model = OrderItem
#         fields = ('id', 'order', 'product_item', 'choice', 'quantity', 'day_out')

class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'

    def create(self, validated_data):
        product_item = validated_data.get('product_item')
        if product_item.quantity < validated_data.get('quantity', 0):
            raise serializers.ValidationError('Bu mahsulot qolmadi!')

        # Deduct stock
        product_item.quantity -= validated_data.get('quantity', 0)
        product_item.save()

        # Create OrderItem
        order_item = OrderItem.objects.create(**validated_data)
        return order_item
