from rest_framework.serializers import ModelSerializer, Serializer, EmailField, CharField
from .models import User
from django.contrib.auth.hashers import make_password

## Verificar que los campos que estamos recibiendo solo sean el email y password
class UserLoginSerializer(Serializer):
    email = EmailField(required=True) 
    password = CharField(required=True)


class UserSerializer(ModelSerializer):
    class Meta:
        # Definir el modelo que usar este Serializer
        model = User
        # Definir cuales son los campos que quiero usar del modelo
        # '__all__' => es igual a decir que vamos a usar todos los campos del modelo
        fields = '__all__'

    def create(self, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(
                validated_data['password'])
        return super().create(validated_data)