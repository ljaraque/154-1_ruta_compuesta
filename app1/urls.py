from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('inicio/', views.index),
    path('', views.principal),
    path('noticias/', views.noticias),
    path('datos/', views.datos),

    path('empresa/', TemplateView.as_view(template_name='app1/empresa.html')),

]
