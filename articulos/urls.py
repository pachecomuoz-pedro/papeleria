from django.urls import path
from articulos.views import lista_articulos,nuevo_articulo,eliminar_articulo,editar_articulo
from .views import eliminar_post

urlpatterns = [
    path('', lista_articulos, name='articulos'),
    path('nuevo', nuevo_articulo, name='nuevo_articulo'),
    path('eliminar/<int:id>', eliminar_articulo, name='eliminar_articulo'),
    path('editar/<int:id>', editar_articulo, name='editar_articulo'),
    path('eliminar_post', eliminar_post, name='eliminar_articulo_post'),
]
