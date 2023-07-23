from django.contrib import admin
from .models import Warehouse, Order, OrderItem


@admin.register(Warehouse)
class WareHouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'blog', 'cat', 'zon', 'prod', 'phone_number', 'email', 'enter_date')
    date_hierarchy = 'enter_date'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'warehouse', 'user', 'phone', 'email', 'day_out')
    date_hierarchy = 'day_out'


@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = ('id', 'order', 'product_item', 'choice', 'quantity', 'get_total', 'day_out')
