from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.TextField(null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)
    is_super_user = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name} {self.lastname} - {self.email}'

    class Meta:
        db_table = 'users'