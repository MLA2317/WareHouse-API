from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WarehouseList, WarehouseCreate, WarehouseRUD, LocationListCreate, OrderList, OrderCreate, OrderRUD, \
    OrderProdCreate, OrderProdList, OrderProdRUD, LeavingCreate, LeavingRUD, LeavingList

# router = DefaultRouter()
# router.register(r'warehouses', WarehouseViewSet)

urlpatterns = [
#
    # path('', include(router.urls)),

    path('warehouse/list/', WarehouseList.as_view()),
    path('warehouse/create/', WarehouseCreate.as_view()),
    path('warehouse/rud/<int:pk>/', WarehouseRUD.as_view()),


    path('location/list-create/', LocationListCreate.as_view()),

    path('order/create/', OrderCreate.as_view()),
    path('order/list/', OrderList.as_view()),
    path('order/rud/<int:pk>/', OrderRUD.as_view()),

    path('order-prod/list/', OrderProdList.as_view()),
    path('order-prod/create/', OrderProdCreate.as_view()),
    path('order-prod/rud/<int:pk>/', OrderProdRUD.as_view()),

    path('leaving/list/', LeavingList.as_view()),
    path('leaving/create/', LeavingCreate.as_view()),
    path('leaving/rud/<int:pk>/', LeavingRUD.as_view()),
]

