from django.shortcuts import render

# Create your views here.
import datetime
import random

def index(request):

    fecha_hora_actual = datetime.datetime.now()
    data = {'contenido_dinamico': str(fecha_hora_actual),
            'contenido_dinamico2': [i for i in range(0,random.randint(2,10))]}
    return render(request, 'app1/index.html', context = data)


def principal(request):
    return render(request, 'app1/principal.html')