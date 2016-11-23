from django.db import models
from django.contrib import admin
from django.utils import timezone

class Marca(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dpi = models.CharField(max_length=13)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=7)
    nombre = models.CharField(max_length=30)
    imagen = models.ImageField(null=True, blank=True,upload_to='fotos')
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE,)
    precio = models.FloatField()
    Existencia = models.IntegerField()

    def __str__(self):
        return self.nombre


class Compra(models.Model):
    cantidad = models.IntegerField()
    fecha_compra = models.DateTimeField(blank=True, null=True)
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE,)
    productos = models.ManyToManyField(Producto, through='CD')

    def __str__(self):
        return self.persona




class CD(models.Model):
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE,)
    compra = models.ForeignKey(Compra,on_delete=models.CASCADE,)
