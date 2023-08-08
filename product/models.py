from django.db import models
from category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=220)
    brand = models.CharField(max_length=221)
    description = models.TextField()
    choice = (
        (1, 'SUM'),
        (2, 'Dollar $')
    )
    choice = models.IntegerField(choices=choice, default=1)
    price = models.DecimalField(decimal_places=3, max_digits=7)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f'{self.id} || {self.name} - {self.price} - {self.quantity} - ({self.choice}). Total: {self.total_price()}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    prod_img = models.ImageField(upload_to='prod_image/')

