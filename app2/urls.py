from django.urls import path
from . import views

app_name = 'app2'

urlpatterns = [
    path('datos/', views.datos, name='datos'),
    path('map/', views.map, name='map'),
    path('especial/', views.Especial.as_view(), name = 'especial')
    
]
