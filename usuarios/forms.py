from django import forms
from .models import Empleado,Municipio

class FormEmpleado(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = ('first_name','last_name','estado','municipio')

class EmailForm(forms.Form):
    asunto = forms.CharField(max_length=100)
    rollo = forms.CharField(widget=forms.Textarea(attrs={'cols':'60', 'rows':'50'}), max_length=1000)
    mail_destinatario = forms.EmailField(max_length=100)
