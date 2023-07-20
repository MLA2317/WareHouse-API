from django.contrib import admin
from .models import Blog, Category, Zona


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'title', 'cat_img')


@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat', 'choice', 'product')


