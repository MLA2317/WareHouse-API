from django.urls import path
from .views import ProductListCreate, ProductRUD, ProductItemListCreate, ProductItemRUD


urlpatterns = [
    path('product/list-create/', ProductListCreate.as_view()),
    path('product/rud/<int:pk>/', ProductRUD.as_view()),

    path('product_item/list-create/', ProductItemListCreate.as_view()),
    path('product-item/rud/<int:pk>/', ProductItemRUD.as_view())
]
