# from django.db import models
# from account.models import Account
# from django.conf import settings
# from category.models import Category
# from product.models import Product
#
#
# class Warehouse(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product, related_name='warehouse_prod')
#     phone_number = models.CharField(max_length=16, verbose_name='Phone Number')
#     email = models.EmailField()
#     location = models.CharField(max_length=125)
#     enter_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.user} - {self.products} - {self.phone_number} - {self.email} - {self.location}'

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
#     def __str__(self):
#         return f'order of {self.customer_id} (id: {self.id}) || {self.warehouse_id}'
#
#
# class OrderProduct(models.Model):
#     order_id = models.ManyToManyField(Order, related_name='order_prod')
#     products = models.ManyToManyField(Product, related_name='order')
#     quantity = models.PositiveIntegerField()
#
#     def __str__(self):
#         return self.order_id
#
#
# class Leaving(models.Model):
#     order_prod_id = models.ForeignKey(OrderProduct, on_delete=models.CASCADE)
#     day_out = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.order_prod_id

