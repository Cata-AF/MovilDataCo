from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    rol = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    numero = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
    