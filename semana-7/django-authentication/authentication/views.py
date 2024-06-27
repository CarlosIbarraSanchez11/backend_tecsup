from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializers import UserSerializer

# Crear la clase UserViewSet Para hacer el CRUD
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer