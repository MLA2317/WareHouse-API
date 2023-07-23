from rest_framework import serializers
from django.core.mail import send_mail
from .models import Warehouse, Order, OrderItem


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ('id', 'user', 'blog', 'cat', 'zon', 'prod', 'phone_number', 'email', 'enter_date')

    def create(self, validated_data):
        warehouse = super().create(validated_data)
        self.send_notification(warehouse)
        return warehouse

    def send_notification(self, warehouse):
        send_mail(
            'Warehouse Company!',
            f'Sizning Mahsulotingiz omborxonada joylandi. Product Nomi: {warehouse.prod.product_name}.',
            'omborxona@gmail.com',
            [warehouse.user.email],
            fail_silently=False,
        )
