from django.contrib import admin
from .models import Warehouse, Order, OrderProduct, Leaving, Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product_names', 'phone_number', 'email', 'location', 'enter_date')
    search_fields = ['user__username', 'phone_number', 'email', 'location']
    list_filter = ('enter_date',)

    def product_names(self, obj):
        return obj.product_names()

    product_names.short_description = 'Products'


class OrderAdmin(admin.ModelAdmin):
    list_display = ('warehouse_names', 'customer_id', 'status')
    search_fields = ['customer_id__username', 'status']
    list_filter = ('status',)

    def warehouse_names(self, obj):
        return obj.warehouse_names()

    warehouse_names.short_description = 'Warehouses'


admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Order, OrderAdmin)

#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'cart', 'phone', 'email', 'address', 'day_out')