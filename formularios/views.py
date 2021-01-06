import json

from django.shortcuts import render, redirect
from .forms import FormularioGuitarra
from django.conf import settings

# Create your views here.

'''
# esta función obtiene la IP del usuario que hace el request
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        print("returning FORWARDED_FOR")
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        print("returning REAL_IP")
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        print("returning REMOTE_ADDR")
        ip = request.META.get('REMOTE_ADDR')
    return ip
'''

def leer_archivo(filename, settings):
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        guitarras=json.load(file)
    return guitarras


def actualizar_archivo(filename, form_data, settings):
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        guitarras=json.load(file)
    guitarras['guitarras'].append(form_data)
    with open(str(settings.BASE_DIR)+filename, 'w') as file:
        json.dump(guitarras, file)

def crear_guitarra(request):
    formulario = FormularioGuitarra(request.POST or None)
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        form_data['fecha_compra']=form_data['fecha_compra'].strftime("%Y-%m-%d")
        filename= "/formularios/data/guitarras.json"
        actualizar_archivo(filename, form_data, settings)
        return redirect('formularios:crear_exitoso')
    context = {'form': formulario}
    return render(request, 'formularios/crear_guitarra.html', context)

def crear_exitoso(request):
    filename= "/formularios/data/guitarras.json"
    guitarras = leer_archivo(filename, settings)
    return render(request, 'formularios/crear_exitoso.html', context=guitarras)