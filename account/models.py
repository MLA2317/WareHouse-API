from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken
from account.manager import AccountManager
from django.conf import settings
from django.utils.safestring import mark_safe
from django.db.models.signals import pre_save, post_save
from product.models import Product


class Account(AbstractUser, PermissionsMixin):
    GENDER = (
        (0, 'None'),
        (1, 'Male'),
        (2, 'Female'),
    )
    ROLE = (
        (0, 'Staff'),
        (1, 'Seller'),
        (2, 'Customer'),
    )
    username = models.CharField(max_length=220, unique=True, verbose_name='Username', db_index=True)
    bio = models.CharField(max_length=221)
    avatar = models.ImageField(upload_to='profile/', null=True, blank=True)
    gender = models.IntegerField(choices=GENDER, default=0)
    role = models.IntegerField(choices=ROLE, default=2)
    is_superuser = models.BooleanField(default=False, verbose_name='Super user')
    is_staff = models.BooleanField(default=False, verbose_name='Staff user')
    is_active = models.BooleanField(default=True, verbose_name='Active user')
    is_customer = models.BooleanField(default=False, verbose_name='Custumer')
    is_seller = models.BooleanField(default=False, verbose_name='Seller')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='Modified Date')

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def image_tag(self):
        if self.avatar:
            return mark_safe(f"<a href='{self.avatar.url}'><img src='{self.avatar.url}' style='height:43px;'/></a>")
        else:
            return 'Image not found'

    @property
    def avatar_url(self):
        if self.avatar:
            if settings.DEBUG:
                return f"{settings.LOCALE_BASE_URL}{self.avatar.url}"
            return f"{settings.PROD_BASE_URL}{self.avatar.url}"
        return None

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data


class MyProduct(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='my_product')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author


def account_post_save(instance, sender, created, *args, **kwargs):
    if created:
        if instance.role == 1:
            instance.is_seller = True
        elif instance.role == 2:
            instance.is_customer = True
        elif instance.role == 0:
            instance.is_staff = True
        else:
            instance.is_staff = False
    instance.save()


post_save.connect(account_post_save, sender=Account)


