from django.db import models

class Articulo(models.Model):
    nombre = models.CharField('Nombre',max_length=100)
    descripcion = models.CharField('Descripción', max_length=300)
    precio = models.DecimalField('Precio Unitario',max_digits=5, decimal_places=2)
    cantidad = models.IntegerField('Cantidad')
    imagen = models.ImageField('Imagen', upload_to='articulos', null=True, blank=True)

    def __str__(self):
        return self.nombre

