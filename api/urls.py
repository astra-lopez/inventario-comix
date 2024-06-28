from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
  ComicViewSet,
  SaleViewSet
)


router = DefaultRouter()
router.register(r'Comic', ComicViewSet, basename='comic')
router.register(r'Sales', SaleViewSet, basename='sales')

urlpatterns = [
    *router.urls,
]