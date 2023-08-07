# from django.contrib import admin
# from .models import Warehouse, Cart, CartItem, Order
#
#
# @admin.register(Warehouse)
# class WareHouseAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'blog', 'cat', 'zon', 'prod', 'phone_number', 'email', 'enter_date')
#     date_hierarchy = 'enter_date'
#
#
# @admin.register(Cart)
# class CartAdmin(admin.ModelAdmin):
#     list_display = ('id', 'client', 'war_prod')
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