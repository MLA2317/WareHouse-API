from django.urls import path
from .views import ProductList, ProductCreate, ProductRUD, ProductItemList, ProductItemCreate, ProductItemRUD


urlpatterns = [
    path('product/list/', ProductList.as_view()),
    path('product/create/', ProductCreate.as_view()),
    path('product/rud/<int:pk>/', ProductRUD.as_view()),

    path('product_item/list/', ProductItemList.as_view()),
    path('product_item/create/', ProductItemCreate.as_view()),
    path('product-item/rud/<int:pk>/', ProductItemRUD.as_view())
]
