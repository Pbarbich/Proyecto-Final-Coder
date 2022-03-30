from django.urls import path
from app_final.views import *

urlpatterns = [
    path('', inicio, name = 'Inicio'),
    path('clientes/', clientes, name = 'Clientes'),
    path('restos/', restos, name = 'Restos'),
    path('menu/', menu, name = 'Menu'),
]    