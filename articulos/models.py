from django.db import models
from django.core.validators import MaxLengthValidator
from articulos.validador import validate_cantidad
LONGITUD_MAXIMA = 'Longitud excedida'


class Articulo(models.Model):
    nombre = models.CharField(
        'Nombre', max_length=100, validators=[MaxLengthValidator(100, LONGITUD_MAXIMA)])
    descripcion = models.CharField('Descripción', max_length=300)
    precio = models.DecimalField(
        'Precio Unitario', max_digits=5, decimal_places=2)
    cantidad = models.IntegerField('Cantidad', validators=[validate_cantidad])
    imagen = models.ImageField(
        'Imagen', upload_to='articulos', null=True, blank=True)

    def __str__(self):
        return self.nombre
