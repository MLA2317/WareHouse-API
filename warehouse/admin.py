# from django.contrib import admin
# from .models import Warehouse, Order, OrderProduct, Leaving
#
#
# class WarehouseAdmin(admin.ModelAdmin):
#     list_display = ('user', 'phone_number', 'email', 'location', 'enter_date')
#     search_fields = ['user__username', 'phone_number', 'email', 'location']
#     list_filter = ('enter_date',)
#
#
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('customer_id', 'status')
#     search_fields = ['customer_id__username', 'status']
#     list_filter = ('status',)
#
#
# admin.site.register(Warehouse, WarehouseAdmin)
# admin.site.register(Order, OrderAdmin)
#
#
# @admin.register(CartItem)
# class CartItemAdmin(admin.ModelAdmin):
#     list_display = ('id', 'carts', 'quantity', 'created_date')
#
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'cart', 'phone', 'email', 'address', 'day_out')