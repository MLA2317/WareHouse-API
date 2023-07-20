from django.db import models
from account.models import Account
from category.models import Blog, Category, Zona
from product.models import Product


class Warehouse(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='war_cat')
    zon = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name='war_zon')
    prod = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='war_prod')
    phone_number = models.CharField(max_length=16, verbose_name='Phone Number')
    email = models.EmailField()
    enter_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.prod.product_name}- {self.prod.prod_item} of {self.user}'


class Order(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    day_out = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.user
    # status = models.CharField(max_length=50, choices=(
    #     ('pending', 'Pending'),
    #     ('processing', 'Processing'),
    #     ('shipped', 'Shipped'),
    #     ('delivered', 'Delivered'),
    #     ('canceled', 'Canceled'),
    # ))


class OrderItem(models.Model):
    Choice = (
        (0, 'KG'),
        (1, 'COUNT')
    )
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_item = models.ForeignKey(Product, on_delete=models.CASCADE)
    choice = models.IntegerField(choices=Choice, default=0)
    quantity = models.PositiveIntegerField(default=0)
    day_out = models.DateTimeField(auto_now_add=True)

    def get_total(self):
        return f'Total - {self.quantity * self.product_item.product_name.product_item.price}'



