from django.urls import path
from . import views

app_name = 'formularios'

urlpatterns = [
    path('crear_guitarra/', views.crear_guitarra, name='crear_guitarra'),
    path('crear_exitoso/', views.crear_exitoso, name='crear_exitoso'),
    path('grafico2/', views.grafico2),
    path('<id>/borrar', views.eliminar_guitarra, name="eliminar_guitarra"),
    path('crear_guitarra_db/', views.crear_guitarra_db, name='crear_guitarra_db'),
    path('lista_guitarras_db', views.lista_guitarras_db, name="lista_guitarras_db"),
    path('<id>/borrar_db', views.eliminar_guitarra_db, name="eliminar_guitarra_db"),
    path('<id>/editar_db', views.editar_guitarra_db, name="editar_guitarra_db"),
    
]
