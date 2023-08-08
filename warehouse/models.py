# from django.db import models
# from account.models import Account
# from django.conf import settings
# from category.models import Category
# from product.models import Product
#
#
# class Location(models.Model):
#     title = models.CharField(max_length=220)
#
#     def __str__(self):
#         return self.title
#
#
# class Warehouse(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product, related_name='warehouse_prod')
#     phone_number = models.CharField(max_length=16, verbose_name='Phone Number')
#     email = models.EmailField()
#     location = models.ForeignKey(Location, on_delete=models.CASCADE)
#     enter_date = models.DateTimeField(auto_now_add=True)
#
#     def product_names(self):
#         return ", ".join([str(p) for p in self.products.all()])
#
#     def __str__(self):
#         return f'{self.user} - {self.products} - {self.phone_number} - {self.email} - {self.location}'
#
#
# class Order(models.Model):
#     STATUS = (
#         ('Cancel', 'Cancelled'),
#         ('Process', 'Process'),
#         ('Shipped', 'Shipped')
#     )
#     warehouse_id = models.ManyToManyField(Warehouse, related_name='order_warehouse')
#     customer_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     status = models.CharField(max_length=7, choices=STATUS)
#
#     def warehouse_names_id(self):
#         return ", ".join([str(w) for w in self.warehouse_id.all()])
#
#     def __str__(self):
#         return f'{self.customer_id} (id: {self.id}) || {self.warehouse_id}'
#
#
# class OrderProduct(models.Model):
#     order_id = models.ManyToManyField(Order, related_name='order_prod')
#     products = models.ManyToManyField(Product, related_name='order')
#     quantity = models.PositiveIntegerField()
#
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         for product in self.products.all():
#             product.quantity -= self.quantity
#             product.save()
#
#
# class Leaving(models.Model):
#     order_prod_id = models.ForeignKey(OrderProduct, on_delete=models.CASCADE)
#     day_out = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.order_prod_id} {self.day_out}'
#
