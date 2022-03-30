from operator import truediv
from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length = 40)
    mail = models.EmailField()
    celular = models.IntegerField(primary_key=True)

class Restaurante(models.Model):
    nombre = models.CharField(max_length = 40)
    mail = models.EmailField(primary_key=True)
    comida = models.CharField(max_length = 40)
    direccion = models.CharField(max_length = 60)

class Menu(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre =  models.CharField(max_length = 40)
    descripcion =  models.CharField(max_length = 100)
    precio = models.IntegerField()

class Plataforma(models.Model):
    empresa = models.CharField(max_length = 40)
    mail = models.EmailField(primary_key=True)