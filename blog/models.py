from django.conf import settings
from django.db import models

class Publicacion(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    imagen = models.URLField(blank=True, null=True)
    apodo = models.TextField(blank=True, null=True)
    altura = models.IntegerField(blank=True, null=True)
    peso = models.TextField(blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    pais = models.TextField(blank=True, null=True)
    categoria = models.TextField(blank=True, null=True)
    record = models.TextField(blank=True, null=True)
    titulos = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

def __str__(self):
    return self.nombre