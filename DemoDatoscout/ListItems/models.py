from django.db import models

# Create your models here.
class Producto(models.Model):
    slug = models.SlugField(unique=True)
    nombre = models.CharField(max_length=100)
    ventas = models.IntegerField(max_length=8)
    crecimiento = models.IntegerField(max_length=8)
    destino = models.CharField(max_length=100)