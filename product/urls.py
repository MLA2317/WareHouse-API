from django.urls import path
from .views import ProductListCreate, ProductItemListCreate


urlpatterns = [
    path('product/', ProductListCreate.as_view()),
    path('product_item/', ProductItemListCreate.as_view())
]