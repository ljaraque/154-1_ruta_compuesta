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
    
    path('lista_guitarras_db_view', views.ListaGuitarraView.as_view(), name="lista_guitarras_db_view"),

    path('<id>/borrar_db', views.eliminar_guitarra_db, name="eliminar_guitarra_db"),
    path('<pk>/borrar_db_cbv', views.EliminarGuitarra.as_view(), name="eliminar_guitarra_db_cbv"),
    path('<id>/editar_db', views.editar_guitarra_db, name="editar_guitarra_db"),

    path('<id>/editar_db_view', views.EditarGuitarraView.as_view(), name="editar_guitarra_db_view"),
    
    path('<pk>/editar_db_cbv', views.EditarGuitarra.as_view(), name="editar_guitarra_db_cbv"),
    path('lista_guitarras_db_cbv', views.ListaGuitarras.as_view(), name="lista_guitarras_db_cbv"),
    path('lista_guitarras_db_cbv_no_auto', views.ListaGuitarrasNoAuto.as_view(), name="lista_guitarras_db_cbv_no_auto"),
    path('crear_guitarra_db_cbv', views.CrearGuitarra.as_view(), name='crear_guitarra_db_cbv'),
    
]
