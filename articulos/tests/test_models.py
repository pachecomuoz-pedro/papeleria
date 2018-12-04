from django.test import TestCase
from articulos.models import Articulo, LONGITUD_MAXIMA
from django.core.exceptions import ValidationError


class TestModels(TestCase):

    def setUp(self, nombre='Cuaderno', descripcion='Doble raya', precio='15.50', cantidad='10'):
        self.articulo = Articulo(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            cantidad=cantidad
        )

    def test_return_object_articulo(self):
        self.articulo.save()
        self.assertEquals(self.articulo.nombre, self.articulo.__str__())

    def test_max_length_nombre(self):
        self.articulo.nombre='Cuadernosddbcjlsbjsdbdbjdbvlakjdsbvdbvñaldsjbajevbkjsbvjhbvlhjbcjbsdvbkjsdcssjdvbkasjdvbkahlshdb'
        self.assertLess(len(self.articulo.nombre), 100)

    def test_longitud_excedida(self):
        self.articulo.nombre='Cuadernosddbcjlsbjsdbdbjddlvfdkjvbvlakjdsbvdbvñaldsjbajevbkjsbvjhbvlhjbcjbsdvbkjsdcssjdvbkasjdvbkahlshdb'
        
        with self.assertRaises(ValidationError):
        	self.articulo.full_clean()

    def test_longitud_excedida_texto_error(self):
        self.articulo.nombre='Cuadernosddbcjlsbjsdbdbjddlvfdkjvbvlakjdsbvdbvñaldsjbajevbkjsbvjhbvlhjbcjbsdvbkjsdcssjdvbkasjdvbkahlshdb'
        
        try:
            self.articulo.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['nombre'][0])
            self.assertEquals(msg, LONGITUD_MAXIMA)

    def test_guardar_articulo(self):
        self.articulo.save()
        self.assertEquals(Articulo.objects.all()[0], self.articulo)

    def test_guardar_nombre_articulo(self):
        self.articulo.save()
        articulo = Articulo.objects.first()
        self.assertEquals(articulo.nombre, 'Cuaderno')
