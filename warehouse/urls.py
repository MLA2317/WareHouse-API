from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WarehouseViewSet, CartViewSet, CartItemViewSet
# from .views import WarehouseCreate, WareHouseList
#
#
# urlpatterns = [
#
# ]
#
#
router = DefaultRouter()
router.register(r'warehouses', WarehouseViewSet)
router.register(r'cart', CartViewSet)
router.register(r'CartItem', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


