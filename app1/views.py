import datetime
import random
import csv
import uuid

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings

# Create your views here.

from django.shortcuts import reverse, redirect
from django.utils.http import urlencode
def datos(request):
    if not request.user.is_authenticated:
        loginurl = reverse('login') + '?' + urlencode({'next':request.path})
        return redirect(loginurl)

    print(request.COOKIES)
    filename= "/app1/data/iris.csv"
    ruta_completa_archivo = str(settings.BASE_DIR)+filename
    with open(ruta_completa_archivo, "r") as archivo:
        data = csv.DictReader(archivo)
        data_list = []
        for elemento in data:
            data_list.append(elemento)
    context = {'datos_desde_archivo': data_list}
    response = render(request, 'app1/datos.html', context)
    response.set_cookie(key='identificador', value=uuid.uuid4(), max_age=365*24*60*60)
    response.set_cookie(key='eltiempo', value='nublado', max_age=20)
    return response


def index(request):
    if 'num_visitas' not in request.session:
        request.session['num_visitas'] = 1
    else:
        request.session['num_visitas'] += 1
    


    fecha_hora_actual = str(datetime.datetime.now())

    #lista_aleatoria = [i for i in range(0,random.randint(2,10))]

    lista = [1,2,3,4,5,6,7]
    nombres = ["Boris", "Jean Carlos", "Jesús", 
                "Jonathan", "Rocío", "Daniela", "Francisca",
                "Roberta", "Nabucodonosorcito", "Albert", "Alan",
                "Topo Giggio", "Tía Patricia", "Tía Pucherito",
                "Jonathan", "Rocío", "Daniela", "Francisca",
                "Roberta", "Nabucodonosorcito", "Albert", "Alan",
                "Topo Giggio", "Tía Patricia", "Tía Pucherito",
                "Jonathan", "Rocío", "Daniela", "Francisca",
                "Roberta", "Nabucodonosorcito", "Albert", "Alan",
                "Topo Giggio", "Tía Patricia", "Tía Pucherito",
                "Jonathan", "Rocío", "Daniela", "Francisca",
                "Roberta", "Nabucodonosorcito", "Albert", "Alan",
                "Topo Giggio", "Tía Patricia", "Tía Pucherito"]

    context = {'contenido_dinamico': fecha_hora_actual,
                'contenido_dinamico2':  lista,
                'nombres': nombres,
                'num_visitas': request.session['num_visitas']
                }
    
    return render(request, 'app1/index.html', context)


def principal(request):
    return render(request, 'app1/principal.html')

def noticias(request):
    # envía una instrucción de redireccionamiento al broswer
    # y browser obedece y realiza un nuevo get a esta url
    return HttpResponseRedirect('https://www.washingtonpost.com')

def prueba(request):
    return render(request, 'app1/base.html')

from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin

class Empresa(LoginRequiredMixin, View):
    def get(self,request):
        return render(request,'app1/empresa.html')

