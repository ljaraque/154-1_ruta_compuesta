from django.urls import path
from . import views

app_name = 'formularios'

urlpatterns = [
    path('crear_guitarra/', views.crear_guitarra, name='crear_guitarra'),
    path('crear_exitoso/', views.crear_exitoso, name='crear_exitoso'),
    path('grafico2/', views.grafico2),
]
