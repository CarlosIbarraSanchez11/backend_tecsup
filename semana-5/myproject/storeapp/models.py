from django.db import models

# Create your models here.
class Category(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    activa = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    ## Muesta el nombre de la categoria en el main web
    def __str__(self) -> str:
        return f"{self.id} {self.nombre}"
    class Meta:
        db_table = 'categories'


class Product(models.Model): # Indica que esto es un modelo
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField( blank=True, null=True)
    stock = models.PositiveBigIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    # category = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # Campo solo de lectura
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta: # Clase internta para cambiar el nombre de la tabla
        db_table = 'products'
    
