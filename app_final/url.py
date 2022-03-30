from django.urls import path
from app_final.models import Plataforma
from app_final.views import *

urlpatterns = [
    path('', inicio, name = 'Inicio'),
    path('clientes/', clientes, name = 'Clientes'),
    path('restos/', restos, name = 'Restos'),
    path('menu/', menu, name = 'Menu'),
    path('sobre-nosotros/', about, name = "About"),
    path('plataforma/', plataforma, name = "Plataforma"),
    path('crear-resto/', formulario_resto, name = "FormularioResto"),
    path('crear-plataforma/', formulario_plataformas, name = "FormularioPlataformas"),
    path('crear-menu/', formulario_menu, name = "FormularioMenu"),
    path('crear-cliente/', formulario_clientes, name = "FormularioClientes"),
    path('buscar-resto/', buscar_resto, name = "FormularioBuscarResto"),
]    