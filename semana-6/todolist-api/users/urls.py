from .views import  UserViewSet, AuthenticationView
from rest_framework.routers import DefaultRouter
from django.urls import UserV

router = DefaultRouter()

router.register(r'users', UserViewSet)

urlpatterns = router.urls