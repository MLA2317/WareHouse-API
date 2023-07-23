from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=2)

    def __str__(self):
        return self.title


class Category(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='blog_cat')
    title = models.CharField(max_length=221)
    cat_img = models.ImageField(upload_to='category/', null=True)

    def __str__(self):
        return f'{self.blog} -  {self.title}'


class Zona(models.Model):
    Zona = (
        (1, 'ZONA 1'),
        (2, 'ZONA 2'),
        (3, 'ZONA 3'),
        (4, 'ZONA 4'),
        (5, 'ZONA 5')
    )
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='zona_cat')
    choice = models.IntegerField(choices=Zona, default=False)
    product = models.CharField(max_length=221)

    def __str__(self):
        return f'{self.cat}, Zona - {self.choice} in {self.product}'





