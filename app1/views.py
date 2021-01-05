import datetime
import random
import csv

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings

# Create your views here.


def datos(request):
    filename= "/app1/data/iris.csv"
    ruta_completa_archivo = str(settings.BASE_DIR)+filename
    with open(ruta_completa_archivo, "r") as archivo:
        data = csv.DictReader(archivo)
        data_list = []
        for elemento in data:
            data_list.append(elemento)
    context = {'datos_desde_archivo': data_list}
    return render(request, 'app1/datos.html', context)


def index(request):

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
                'nombres': nombres}
    
    return render(request, 'app1/index.html', context)


def principal(request):
    return render(request, 'app1/principal.html')

def noticias(request):
    # envía una instrucción de redireccionamiento al broswer
    # y browser obedece y realiza un nuevo get a esta url
    return HttpResponseRedirect('https://www.washingtonpost.com')

def prueba(request):
    return render(request, 'app1/base.html')