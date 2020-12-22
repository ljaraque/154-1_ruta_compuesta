from django.shortcuts import render

# Create your views here.

def concinero_inicio(request):
    return render(request, 'app1/hamburguesa.html')