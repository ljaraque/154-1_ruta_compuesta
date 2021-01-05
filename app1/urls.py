from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'app1'

urlpatterns = [
    path('inicio/', views.index, name="inicio"),
    path('', views.principal),
    path('noticias/', views.noticias),
    path('datos/', views.datos, name='datos'),
    path('prueba/', views.prueba),

    path('empresa/', TemplateView.as_view(template_name='app1/empresa.html'), name='empresa'),

]
