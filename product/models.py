from django.db import models
from category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=220)
    brand = models.CharField(max_length=221)
    description = models.TextField()
    choice = (
        (1, 'SUM'),
        (2, '$')
    )
    choice = models.IntegerField(choices=choice, default=1)
    price = models.DecimalField(decimal_places=3, max_digits=7)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} || {self.name} - {self.price} ({self.choice})'
#
#
# class ProductImage(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
#     prod_img = models.ImageField(upload_to='prod_image/')
#
#
# # class ProductItem(models.Model):
# #     Choice = (
# #         (1, 'KG'),
# #         (2, 'COUNT')
# #     )
# #     products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prod_item')
# #     choice = models.IntegerField(choices=Choice, default=1)
# #     quantity = models.IntegerField(default=0)
# #     created_date = models.DateTimeField(auto_created=True)
# #
# #     def __str__(self):
# #         return f'Product - {self.products}, Choice {self.choice} - {self.quantity}, Total - {self.products.price * self.quantity}'
#
#
#
#
#
#
#
#
#
