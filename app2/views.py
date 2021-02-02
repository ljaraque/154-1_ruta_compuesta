from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required(login_url='/accounts/login/')
def datos(request):
    return render(request, 'app2/index.html')

def map(request):
    return render(request, 'app2/map.html')



'''
def usuario_permitido(usuario):
    es_admin = usuario.is_superuser
    return es_admin
'''

def usuario_permitido(usuario):
    if usuario.profile.rol == "estudiante":
        validacion = True
    else:
        validacion = False
    return validacion

from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class Especial(LoginRequiredMixin,UserPassesTestMixin, View):
    def test_func(self):
        return usuario_permitido(self.request.user)

    def get(self,request):
        return render(request,'app2/especial.html')

