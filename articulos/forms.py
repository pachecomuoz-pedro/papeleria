from django import forms
from .models import Articulo

class FormArticulo(forms.ModelForm):

    class Meta:
        model = Articulo
        fields = ('nombre','descripcion','precio','cantidad','imagen')





