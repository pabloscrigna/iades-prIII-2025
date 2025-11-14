from django.db import models


# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField()
    apellido = models.CharField()
    dni = models.IntegerField()
    creado = models.DateTimeField(auto_now_add=True)