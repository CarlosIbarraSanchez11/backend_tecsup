from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    # Permite crear una tupla con los campos que queremos mostrar en el admin
    list_display = ('id', 'name', 'description', 'price', 'stock','category')
    list_filter = ('category',)

admin.site.register(Product, ProductAdmin)
# Register your models here.
