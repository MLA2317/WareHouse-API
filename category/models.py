from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=2)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=221)
    cat_img = models.ImageField(upload_to='category/', null=True)

    def __str__(self):
        return self.title


class Zona(models.Model):
    Choice = (
        (1, 'ZONA 1'),
        (2, 'ZONA 2'),
        (3, 'ZONA 3'),
        (4, 'ZONA 4'),
        (5, 'ZONA 5')
    )
    zona = models.IntegerField(choices=Choice, default=False)
    product = models.CharField(max_length=221)

    def __str__(self):
        return f'zona {self.zona} || {self.product}'





