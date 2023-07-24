from django.db import models
from account.models import Account
from category.models import Blog, Category, Zona
from product.models import Product, ProductItem


class Warehouse(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='war_cat')
    zon = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name='war_zon')
    prod = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='war_prod')
    phone_number = models.CharField(max_length=16, verbose_name='Phone Number')
    email = models.EmailField()
    enter_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.prod}{self.prod.quantity} - {self.phone_number} - {self.email} - {self.enter_date}'


class Cart(models.Model):
    client = models.ForeignKey(Account, on_delete=models.CASCADE)
    war_prod = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.client} || {self.war_prod}'


class CartItem(models.Model):
    carts = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.carts} || Total : {self.quantity * self.carts.war_prod.prod.products.price} Choice {self.carts.war_prod.prod.products.choice}'


class Order(models.Model):
    cart = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=220)
    day_out = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} || {self.cart} || {self.phone} || {self.email} || {self.day_out}'



#
# class Cart(models.Model):
#     clients = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='cart')
#     is_ordered = models.BooleanField(default=False)
#
#     @property
#     def get_cart_items(self):
#         cart_items = self.cart_items.all()
#         total = sum([item.quantity for item in cart_items])
#         return total
#
#     @property
#     def get_cart_total(self):
#         cart_items = self.cart_items.all()
#         total = sum([item.get_item_total for item in cart_items])
#         return total
#
#     def __str__(self):
#         return f"cart of {self.clients} (id: {self.id})"
#
#
# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
#     warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     created_date = models.DateTimeField(auto_now_add=True)
#
#     @property
#     def get_item_total(self):
#         return f'Your cart - {self.warehouse.prod.products.name}, Total -{self.quantity * self.warehouse.prod.products.price}'
