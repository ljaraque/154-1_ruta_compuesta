import json

from django.shortcuts import render, redirect
from .forms import FormularioGuitarra
from django.conf import settings
from .models import Guitarra, GuitarraCBV
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import View

# Create your views here.

'''
# esta función obtiene la IP del usuario que hace el request
def get_clierimerFormulariont_ip(request):
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


#CRUD: Crear guitarra con vista basada en función y archivo de datos
def crear_guitarra(request):
    formulario = FormularioGuitarra(request.POST or None)
    context = {'form': formulario}
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        form_data['fecha_compra']=form_data['fecha_compra'].strftime("%Y-%m-%d")
        filename= "/formularios/data/guitarras.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            guitarras=json.load(file)
        form_data['id'] = guitarras['ultimo_id_generado'] + 1
        guitarras['ultimo_id_generado'] = form_data['id']
        guitarras['guitarras'].append(form_data)
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(guitarras, file)
        return redirect('formularios:crear_exitoso')
    return render(request, 'formularios/crear_guitarra.html', context)

#CRUD: Lista de guitarras con vista basada en función y archivo de datos
def crear_exitoso(request):
    filename= "/formularios/data/guitarras.json"
    guitarras = leer_archivo(filename, settings)
    return render(request, 'formularios/crear_exitoso.html', context=guitarras)


def grafico2(request):
    lista = []
    lista_modelo = []
    filename= "/formularios/data/guitarras.json"
    with open(str(settings.BASE_DIR)+filename, "r") as file:
        guitarras=json.load(file)
        diccionario = guitarras.get('guitarras')
        for elemento in diccionario[-5:]:
            cuerdas = elemento.get('cuerdas')
            modelo = elemento.get('modelo')
            lista.append(cuerdas)
            lista_modelo.append(modelo)
    print(lista_modelo)
    context = {'modelo': lista_modelo, 'valor' : lista}
    return render(request, "formularios/grafico2.html", context)


#CRUD: Eliminar guitarra con vista basada en función y archivo de datos
def eliminar_guitarra(request, id):
    if request.method == "POST":
        filename= "/formularios/data/guitarras.json"
        with open(str(settings.BASE_DIR)+filename, "r") as file:
            guitarras=json.load(file)
        for guitarra in guitarras['guitarras']:
            print(int(guitarra['id']), int(id))
            if int(guitarra['id']) == int(id):
                guitarras['guitarras'].remove(guitarra)
                break
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(guitarras, file)
        return redirect('formularios:crear_exitoso')
    context = {'id': id} 
    return render(request, "formularios/eliminar_guitarra.html", context)


#CRUD: Crear guitarra con vista basada en función y base de datos
def crear_guitarra_db(request):
    formulario = FormularioGuitarra(request.POST or None)
    context = {'form': formulario}
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        form_data['fecha_compra']=form_data['fecha_compra'].strftime("%Y-%m-%d")
        Guitarra.objects.create(
                        modelo = form_data['modelo'],
                        marca = form_data['marca'],
                        cuerdas = form_data['cuerdas'],
                        fecha_compra = form_data['fecha_compra']
                        )
        return redirect('formularios:lista_guitarras_db')
    return render(request, 'formularios/crear_guitarra_db.html', context)


#CRUD: Editar guitarras con vista basada en función y base de datos
def editar_guitarra_db(request, id):
    guitarra = Guitarra.objects.filter(id=id).values()[0]
    formulario = FormularioGuitarra(request.POST or None, initial=guitarra)
    context = {'form': formulario, 'id':id}
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        form_data['fecha_compra']=form_data['fecha_compra'].strftime("%Y-%m-%d")
        Guitarra.objects.filter(id=id).update(
                        modelo = form_data['modelo'],
                        marca = form_data['marca'],
                        cuerdas = form_data['cuerdas'],
                        fecha_compra = form_data['fecha_compra']
                        )
        return redirect('formularios:lista_guitarras_db')
    return render(request, 'formularios/editar_guitarra_db.html', context)


class EditarGuitarraView(View):
    def get(self, request, pk):
        guitarra = Guitarra.objects.filter(id=pk).values()[0]
        formulario = FormularioGuitarra(initial=guitarra)
        context = {'form': formulario, 'id':pk}
        return render(request, 'formularios/editar_guitarra_db_view.html', context)

    def post(self, request, pk):
        formulario = FormularioGuitarra(request.POST) 
        if formulario.is_valid():
            form_data = formulario.cleaned_data
            form_data['fecha_compra']=form_data['fecha_compra'].strftime("%Y-%m-%d")
            Guitarra.objects.filter(id=pk).update(
                            modelo = form_data['modelo'],
                            marca = form_data['marca'],
                            cuerdas = form_data['cuerdas'],
                            fecha_compra = form_data['fecha_compra']
                            )
            return redirect('formularios:lista_guitarras_db_view')
        
        
class ListaGuitarraView(View):
    def get(self, request):
        lista_guitarras = list(Guitarra.objects.all().values())
        context = {'guitarras': lista_guitarras}
        return render(request, 'formularios/lista_guitarras_db_view.html', context=context)


#CRUD: Lista de guitarras con vista basada en función y base de datos
def lista_guitarras_db(request):
    lista_guitarras = list(Guitarra.objects.all().values())
    context = {'guitarras': lista_guitarras}
    return render(request, 'formularios/lista_guitarras_db.html', context=context)


#CRUD: Eliminar guitarra con vista basada en función y base de datos
def eliminar_guitarra_db(request, id):
    if request.method == "POST":
        Guitarra.objects.filter(id=id).delete()
        return redirect('formularios:lista_guitarras_db')
    context = {'id': id} 
    return render(request, "formularios/eliminar_guitarra_db.html", context)


#CRUD: Vistas basadas en clases CBV
class ListaGuitarras(ListView):
    model = GuitarraCBV


class ListaGuitarrasNoAuto(ListView):
    model = GuitarraCBV
    context_object_name = 'guitarras'
    extra_context = {'mensaje_especial':'ListView menos automatizada '}
    template_name = 'formularios/guitarracbv_list_no_auto.html'


class CrearGuitarra(CreateView):
    model = GuitarraCBV
    fields = '__all__'
    success_url = reverse_lazy('formularios:lista_guitarras_db_cbv')


class EditarGuitarra(UpdateView):
    model = GuitarraCBV
    fields = '__all__'
    success_url = reverse_lazy('formularios:lista_guitarras_db_cbv')


class EliminarGuitarra(DeleteView):
    model = GuitarraCBV
    success_url = reverse_lazy('formularios:lista_guitarras_db_cbv')
    
