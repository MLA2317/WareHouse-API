from rest_framework import serializers
from django.core.mail import send_mail
from .models import Warehouse
from category.serializer import CategorySerializer

#
# class WarehouseGETSerializer(serializers.ModelSerializer):
#     cat = CategorySerializer(read_only=True)
#     prod = ProductItemGETSerializer(read_only=True)
#
#     class Meta:
#         model = Warehouse
#         fields = ('id', 'user', 'blog', 'cat', 'zon', 'prod', 'phone_number', 'email', 'enter_date')
#
#     def create(self, validated_data):
#         warehouse = super().create(validated_data)
#         self.send_notification(warehouse)
#         return warehouse
#
#     def send_notification(self, Warehouse):
#         send_mail(
#             'Warehouse Company!',
#             f'Sizning Mahsulotingiz omborxonada joylandi. Mahsulot Nomi: {Warehouse.prod.product_name}.',
#             'omborxona@gmail.com',
#             [Warehouse.email],
#             fail_silently=False,
#         )

#
# class WarehousePOSTSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Warehouse
#         fields = ('id', 'user', 'blog', 'cat', 'zon', 'prod', 'phone_number', 'email', 'enter_date')
