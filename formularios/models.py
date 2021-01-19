from django.db import models

# Create your models here.

class Musico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    banda = models.CharField(max_length=50)
    pais =  models.CharField(max_length=50)


class Guitarra(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50)
    cuerdas = models.IntegerField()
    madera = models.CharField(max_length=50, default="No definida")
    fecha_compra = models.DateField()
    musico = models.ForeignKey(Musico, on_delete = models.CASCADE)

