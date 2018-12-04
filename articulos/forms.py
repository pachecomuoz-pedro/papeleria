from django import forms
from .models import Articulo, LONGITUD_MAXIMA
from django.forms import TextInput


class FormArticulo(forms.ModelForm):

    class Meta:
        model = Articulo
        fields = ('nombre', 'descripcion', 'precio', 'cantidad', 'imagen')

        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'precio': TextInput(attrs={'class': 'form-control'}),
            'cantidad': TextInput(attrs={'class': 'form-control'}),
        }

        error_messages={
            'nombre': {'max_length':LONGITUD_MAXIMA, 'required':'El nombre es requerido'}
        }
