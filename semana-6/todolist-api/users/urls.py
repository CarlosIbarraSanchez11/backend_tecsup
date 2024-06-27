from .views import  UserViewSet, AuthenticationView
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'users', UserViewSet)

# urlpatterns = router.urls
urlpatterns =[
    path(r'login', AuthenticationView.as_view(), name='custom'),
    *router.urls
]