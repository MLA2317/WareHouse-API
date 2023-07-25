from rest_framework import serializers
from django.core.mail import send_mail
from .models import Warehouse, Cart, CartItem, Order
from product.serializer import ProductItemGETSerializer
from category.serializer import BlogSerializer, CategorySerializer, ZonaSerializer


class WarehouseSerializer(serializers.ModelSerializer):
    blog = BlogSerializer(read_only=True)
    cat = CategorySerializer(read_only=True)
    zon = ZonaSerializer(read_only=True)
    prod = ProductItemGETSerializer(read_only=True)

    class Meta:
        model = Warehouse
        fields = ('id', 'user', 'blog', 'cat', 'zon', 'prod', 'phone_number', 'email', 'enter_date')

    def create(self, validated_data):
        warehouse = super().create(validated_data)
        self.send_notification(warehouse)
        return warehouse

    def send_notification(self, Warehouse):
        send_mail(
            'Warehouse Company!',
            f'Sizning Mahsulotingiz omborxonada joylandi. Mahsulot Nomi: {Warehouse.prod.product_name}.',
            'omborxona@gmail.com',
            [Warehouse.email],
            fail_silently=False,
        )


class CartGETSerializer(serializers.ModelSerializer):
    war_prod = WarehouseSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'client', 'war_prod')


class CartPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'client', 'war_prod')


class CartItemGETSerializer(serializers.ModelSerializer):
    carts = CartGETSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ('id', 'carts', 'quantity', 'created_date')


class CartItemPOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ('id', 'carts', 'quantity', 'created_date')


class OrderGETSerializer(serializers.ModelSerializer):
    cart = CartItemGETSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'cart', 'phone', 'email', 'address', 'day_out')


class OrderPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'cart', 'phone', 'email', 'address', 'day_out')