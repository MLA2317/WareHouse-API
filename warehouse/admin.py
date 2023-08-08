# from django.contrib import admin
# from .models import Warehouse, Order, OrderProduct, Leaving, Location
# from product.models import Product
#
#
# @admin.register(Location)
# class LocationAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title']
#
#
# @admin.register(Warehouse)
# class WarehouseAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'product_names', 'phone_number', 'email', 'location', 'enter_date')
#     search_fields = ['user__username', 'phone_number', 'email', 'location']
#     list_filter = ('enter_date',)
#
#     def product_names(self, obj):
#         return obj.product_names()
#
#     product_names.short_description = 'Products'
#
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('warehouse_names_id', 'customer_id', 'status')
#     search_fields = ['customer_id__username', 'status']
#     list_filter = ('status',)
#
#     def warehouse_names(self, obj):
#         return obj.warehouse_names()
#
#     warehouse_names.short_description = 'Warehouse'
#
#
# # class OrderProductAdmin(admin.ModelAdmin):
# #     list_display = ('Order', 'quantity')
# #     search_fields = ['order_id__customer_id__username', 'order_id__status', 'quantity']
# #     list_filter = ('order_id__status',)
# #
# #     def order(self, obj):
# #         return obj.warehouse_names()
# #
# #     order.short_description = 'Order'
#
#
# admin.site.register(OrderProduct)
#
#
# @admin.register(Leaving)
# class LeavingAdmin(admin.ModelAdmin):
#     list_display = ['id', 'order_prod_id', 'day_out']
#     search_fields = ['order_prod_id']
#     list_filter = ('day_out',)
#
