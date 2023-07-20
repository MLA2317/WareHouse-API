from django.urls import path
from .views import BlogListCreate, CategoryListCreate, ZonaListCreate


urlpatterns = [
    path('blog/', BlogListCreate.as_view()),
    path('category/', CategoryListCreate.as_view()),
    path('Zona/', ZonaListCreate.as_view())
]