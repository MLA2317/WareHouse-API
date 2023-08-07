from django.urls import path
from .views import ProductList, ProductCreate, ProductRUD, ProductImageCreate


urlpatterns = [
    path('product/list/', ProductList.as_view()),
    path('product/create/', ProductCreate.as_view()),
    path('product/rud/<int:pk>/', ProductRUD.as_view()),

    path('prod-img/create/', ProductImageCreate.as_view()),
]
