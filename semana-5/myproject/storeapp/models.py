from django.db import models

# Create your models here.

class Product(models.Model): # Indica que esto es un modelo
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    stock = models.PositiveBigIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # Campo solo de lectura
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta: # Clase internta para cambiar el nombre de la tabla
        db_table = 'products'