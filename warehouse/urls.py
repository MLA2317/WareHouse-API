from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WarehouseViewSet, CartCreate, CartList, CartRUD, CartItemCreate, CartItemList, CartItemRUD, OrderList, \
    OrderRUD, OrderCreate


router = DefaultRouter()
router.register(r'warehouses', WarehouseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cart/list/', CartList.as_view()),
    path('cart/create/', CartCreate.as_view()),
    path('cart/rud/<int:pk>/', CartRUD.as_view()),

    path('cartItem/list/', CartItemList.as_view()),
    path('cartItem/create/', CartItemCreate.as_view()),
    path('cartItem/rud/<int:pk>/', CartItemRUD.as_view()),

    path('order/list/', OrderList.as_view()),
    path('order/create/', OrderCreate.as_view()),
    path('order/rud/<int:pk>/', OrderRUD.as_view()),
]


