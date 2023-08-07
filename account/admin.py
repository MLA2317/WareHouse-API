from django.contrib import admin
from .models import Account, MyProduct
from .forms import AccountChangeForms, AccountFormsCreate


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    add_form = AccountFormsCreate
    form = AccountChangeForms
    list_display = ['id', 'username', 'image_tag', 'bio', 'gender', 'role', 'is_superuser',
                    'is_staff', 'is_active', 'is_seller', 'is_customer', 'created_date', 'modified_date']


@admin.register(MyProduct)
class MyHistoryJobAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'products', 'created_date']
