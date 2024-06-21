from .views import TaskViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls