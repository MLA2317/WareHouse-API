from django.db import models
from account.models import Account
from category.models import Category
from product.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver


class Warehouse(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    #blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='war_cat')
    #zon = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name='war_zon')
    #prod = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='war_prod')
    phone_number = models.CharField(max_length=16, verbose_name='Phone Number')
    email = models.EmailField()
    enter_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.prod}{self.prod.quantity} - {self.phone_number} - {self.email} - {self.enter_date}'

#
# class Cart(models.Model):
#     client = models.ForeignKey(Account, on_delete=models.CASCADE)
#     war_prod = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.client} || {self.war_prod}'
#
#
# class CartItem(models.Model):
#     carts = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     # prod = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=0)
#     created_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.carts} || Total : {self.quantity * self.carts.war_prod.prod.products.price} Choice {self.carts.war_prod.prod.products.choice}'
#
#     def save(self, *args, **kwargs):
#         self.carts.war_prod.prod.quantity -= self.quantity
#         self.carts.war_prod.prod.save()
#         super().save(*args, **kwargs)
#
#
# class Order(models.Model):
#     cart = models.ForeignKey(CartItem, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=15)
#     email = models.EmailField()
#     address = models.CharField(max_length=220)
#     day_out = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.id} || {self.cart} || {self.phone} || {self.email} || {self.day_out}'
#
#
# # @receiver(post_save, sender=CartItem)
# # def update_product_quantity(sender, instance, **kwargs):
# #     instance.prod.quantity -= instance.quantity
# #     instance.prod.save()
#
