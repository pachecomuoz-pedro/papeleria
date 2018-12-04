from django.shortcuts import render, redirect
from articulos.models import Articulo
from .forms import FormArticulo
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(redirect_field_name='login')
def lista_articulos(context):
    articulos = Articulo.objects.all()
    return render(context, 'articulos.html', {'articulos': articulos})


def nuevo_articulo(context):
    if (context.method == 'POST'):
        form = FormArticulo(context.POST, context.FILES)
        if form.is_valid():
            articulo = form.save()
            articulo.save()
            return redirect('articulos')
        else:
            form = FormArticulo()
    else:
        form = FormArticulo()
    return render(context, 'nuevo_articulo.html', {'formualario': form, 'accion': 'Nuevo'})


def eliminar_articulo(context, id):
    articulo = Articulo.objects.get(pk=id)
    articulo.delete()
    return redirect('articulos')


def editar_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)
    if request.method == "POST":
        form = FormArticulo(request.POST, instance=articulo)
        if form.is_valid():
            articulo = form.save()
            articulo.save()
            return redirect('articulos')
    else:
        form = FormArticulo(instance=articulo)
    return render(request, 'nuevo_articulo.html', {'formualario': form, 'accion': 'Editar'})


def eliminar_post(request):
    id = request.POST.get('id_articulo', None)
    articulo = Articulo.objects.get(pk=id)
    articulo.delete()
    return redirect('articulos')
