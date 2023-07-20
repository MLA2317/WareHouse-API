from django.db import models
from category.models import Zona


class Product(models.Model):
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name='zona_product_item')
    brand = models.CharField(max_length=221)
    product_name = models.CharField(max_length=220)
    prod_img = models.ImageField(upload_to='product_item/')
    description = models.TextField()

    def __str__(self):
        return f'{self.zona} -- {self.brand} -- {self.product_name}'


class ProductItem(models.Model):
    Choice = (
        (1, 'KG'),
        (2, 'COUNT')
    )
    product_item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prod_item')
    choice = models.IntegerField(choices=Choice, default=1)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(decimal_places=3, max_digits=7)
    created_date = models.DateTimeField(auto_created=True)

    def __int__(self):
        return f'{self.product_item.product_name}, Total - {self.quantity * self.product_item.price}'




