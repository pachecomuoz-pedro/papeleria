from django.urls import path
from .views import nuevo, lista_empleados, carga_municipio, enviar_mail

urlpatterns = [
    path('', lista_empleados, name='empleados'),
    path('nuevo', nuevo, name='nuevo_empleado'),
    path('carga_mun', carga_municipio, name='carga_municipio'),
    path('mail', enviar_mail, name='enviar_mail'),
    #path('eliminar/<int:id>', eliminar_articulo, name='eliminar_articulo'),
    #path('editar/<int:id>', editar_articulo, name='editar_articulo'),
]
