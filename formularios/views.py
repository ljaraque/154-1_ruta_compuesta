from django.shortcuts import render
from .forms import FormularioGuitarra

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

def crear_guitarra(request):
    data_post =  dict(request.POST)
    print("\nNUEVO REGISTRO HA LLEGADO!!!!")
    for clave, valor in data_post.items():
        print(clave, ": ", valor)
    #print(get_client_ip(request)) # muestra IP del usuario
    formulario = FormularioGuitarra()
    context = {'form': formulario}
    return render(request, 'formularios/crear_guitarra.html', context)