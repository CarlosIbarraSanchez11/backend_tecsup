# from django.urls import path
# from .views import get_products


# _____
# importar nuestra clase viewset
from .views import ProductViewSet, CategoryViewSet
# importar el router de DRF (Django Rest Framework)
from rest_framework.routers import DefaultRouter

# crear una instancia de DefaultRouter
router = DefaultRouter()
# agregar una ruta usando router
router.register(r'products', ProductViewSet)

# Agregar ruta para category
router.register(r'category', CategoryViewSet)

urlpatterns = router.urls