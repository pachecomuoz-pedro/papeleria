from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Estado(models.Model):
    estado = models.CharField('Estado', max_length=100)

    def __str__(self):
        return self.estado


class Municipio(models.Model):
    municipio = models.CharField('Municipio', max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.municipio


class Empleado(User):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
