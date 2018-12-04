from django.http import HttpResponse
import simplejson
from django.shortcuts import render, redirect
from .models import Empleado, Estado, Municipio
from .forms import FormEmpleado, EmailForm
from django.core.mail import EmailMessage


def nuevo(request):
    if (request.method == 'POST'):
        form = FormEmpleado(request.POST)

        id_municipio = request.POST.get('municipio')

        if form.is_valid():
            empleado = form.save()
            empleado.save()

            return redirect('empleados')
    else:
        form = FormEmpleado()
    return render(request, 'nuevo_empleado.html', {'form': form, 'accion': 'Nuevo'})


def lista_empleados(context):
    empleados = Empleado.objects.all()
    return render(context, 'empleados.html', {'empleados': empleados})


# pip install simplejson


def carga_municipio(request):
    estado = Estado.objects.get(id=request.GET.get('id', ''))

    municipios = Municipio.objects.filter(estado=estado)
    municipiosJson = []
    for municipio in municipios:
        municipiosJson.append(
            {
                'id': municipio.id,
                'municipio': municipio.municipio
            }
        )

    data = simplejson.dumps(municipiosJson)
    return HttpResponse(data, content_type="application/json")


def enviar_mail(request):
    if (request.method == 'POST'):
        form = EmailForm(request.POST)

        if form.is_valid():
            asunto = request.POST.get('asunto', None)
            rollo = request.POST.get('rollo', None)
            destinatario = request.POST.get('mail_destinatario', None)

            email = EmailMessage(
                asunto,
                rollo,
                'pachecomuoz.pedro97@gmail.com',
                [destinatario],
            )
            from django.conf import settings
            ruta = settings.MEDIA_ROOT + '/images/image.png'

            email.attach_file(ruta)
            email.send()

            return redirect('articulos')
    else:
        form = EmailForm()
    return render(request, 'mail.html', {'form': form})
