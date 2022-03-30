import http
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    dict_inicio = {'mensaje': "Bienvenido a Delivery Now!", 'submensaje': "La compañia de delivery más rápida del mercado"}
    return render(request, "app_final/index.html", dict_inicio)

def clientes(request):
    dict_clientes = {'mensaje': "Usa Delivery Now hoy!", 'submensaje': ""}
    return render(request, "app_final/vista_clientes.html", dict_clientes)

def restos(request):
    dict_resto = {'mensaje': "Nuestros Restaurantes", 'submensaje': ""}
    return render(request, "app_final/vista_restos.html", dict_resto)

def menu(request):
    dict_menu = {'mensaje': "Nuestro Menu", 'submensaje': "Elegi que queres comer hoy"}
    return render(request, "app_final/vista_menu.html", dict_menu)
