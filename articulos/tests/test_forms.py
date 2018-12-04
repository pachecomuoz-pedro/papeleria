from django.test import TestCase
from articulos.models import Articulo, LONGITUD_MAXIMA
from articulos.forms import FormArticulo


class TestForms(TestCase):

    def setUp(self, nombre='Cuaderno', descripcion='Doble raya', precio='15.50', cantidad='30'):
        self.data = {
            'nombre': nombre,
            'descripcion': descripcion,
            'precio': precio,
            'cantidad': cantidad
        }
    
    def test_formulario_invalido(self):
        self.data['nombre'] = 'Cuadernosddbcjlsbjsdbdbjddlvfdkjvbvlakjdsbvdbvñaldsjbajevbkjsbvjhbvlhjbcjbsdvbkjsdcssjdvbkasjdvbkahlshdb'
        form = FormArticulo(self.data)
        self.assertFalse(form.is_valid())

    def test_formulario_valido(self):
        form = FormArticulo(self.data)
        self.assertTrue(form.is_valid())

    def test_max_length_nombre(self):
        self.data['nombre'] = 'Cuadernosddbcjlsbjsdbdbjddlvfdkjvbvlakjdsbvdbvñaldsjbajevbkjsbvjhbvlhjbcjbsdvbkjsdcssjdvbkasjdvbkahlshdb'
        form = FormArticulo(self.data)
        self.assertEquals(form.errors['nombre'], [LONGITUD_MAXIMA])

    def test_cantidad_menor_20(self):
        self.data['cantidad'] = 3
        form = FormArticulo(self.data)
        self.assertEquals(form.errors['cantidad'], ['Error {0} es menor a 20'.format(self.data['cantidad'])])
