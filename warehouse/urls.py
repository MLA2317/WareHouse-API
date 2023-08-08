# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import WarehouseListCreate, WarehouseRUD, LocationListCreate, OrderListCreate, OrderRUD, OrderProdCreateList,\
#     OrderProdRUD, LeavingList, LeavingCreate, LeavingRUD
#
# # router = DefaultRouter()
# # router.register(r'warehouses', WarehouseViewSet)
#
# urlpatterns = [
#
#     # path('', include(router.urls)),
#
#     path('warehouse/list-create/', WarehouseListCreate.as_view()),
#     path('warehouse/rud/<int:pk>/', WarehouseRUD.as_view()),
#
#
#     path('location/list-create/', LocationListCreate.as_view()),
#
#     path('order/create-list/', OrderListCreate.as_view()),
#     path('order/rud/<int:pk>/', OrderRUD.as_view()),
#
#     path('order-prod/list-create/', OrderProdCreateList.as_view()),
#     path('order-prod/rud/<int:pk>/', OrderProdRUD.as_view()),
#
#     path('leaving/list/', LeavingList.as_view()),
#     path('leaving/create/', LeavingCreate.as_view()),
#     path('leaving/rud/<int:pk>/', LeavingRUD.as_view()),
# ]
#
