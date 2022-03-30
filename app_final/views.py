import http
from http.client import HTTPResponse
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render

from app_final import forms
from app_final.models import Clientes, Restaurante, Menu, Plataforma
from app_final.forms import Formulario_clientes, Formulario_menu, Formulario_plataformas, Formulario_resto

# Create your views here.

#Paginas de Modelos
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

def about(request):
    dict_about = {'mensaje': "Sobre Nosotros", 'submensaje': ""}
    return render(request, "app_final/about.html", dict_about)

def plataforma(request):
    dict_about = {'mensaje': "Plataforma", 'submensaje': "Conoce las apps con las que ya trabajamos"}
    return render(request, "app_final/vista_plataforma.html", dict_about)


#Formularios Creacion de Datos
def formulario_resto(request):


    if request.method == 'POST':
        form_resto = Formulario_resto(request.POST)

        if form_resto.is_valid:

            data = form_resto.cleaned_data

            resto_nuevo = Restaurante(nombre = data['nombre'],mail = data['mail'], comida = data['comida'], direccion = data['direccion'])
            resto_nuevo.save()

        return render(request, "app_final/formulario_restos.html")

    else:

        form_resto = Formulario_resto()
        
        return render(request, "app_final/formulario_restos.html", {"form_resto": form_resto})

def formulario_plataformas(request):

    if request.method == 'POST':
       form_plataforma = Formulario_plataformas(request.POST)

       if form_plataforma.is_valid:
           data = form_plataforma.cleaned_data

           nueva_plataforma = Plataforma(empresa = data['empresa'], mail = data['data'])
           nueva_plataforma.save()
           
           return render(request, "app_final/formulario_plataformas.html")
           
    else:
        
        form_plataforma = Formulario_plataformas()
        
        return render(request, "app_final/formulario_plataformas.html", {"form_plataforma": form_plataforma})

def formulario_menu(request):

    if request.method == 'POST':

        form_menu = Formulario_menu(request.POST)

        if form_menu.is_valid:

            data = form_menu.cleaned_data

            menu_nuevo = Menu(nombre = data['nombre'], descripcion = data['descripcion'], precio = data['precio'])
            menu_nuevo.save()

        return render(request, "app_final/formulario_restos.html")

    else:

        form_menu = Formulario_menu()
        
        return render(request, "app_final/formulario_menu.html", {"form_menu": form_menu})

def formulario_clientes(request):


    if request.method == 'POST':
        form_clientes = Formulario_clientes(request.POST)

        if form_clientes.is_valid:

            data = form_clientes.cleaned_data

            clientes_nuevo = Clientes(nombre = data['nombre'],mail = data['mail'], celular = data['celular'])
            clientes_nuevo.save()

        return render(request, "app_final/formulario_clientes.html")

    else:

        form_clientes = Formulario_clientes()
        
        return render(request, "app_final/formulario_clientes.html", {"form_clientes": form_clientes})


#Formularios Recuperar Datos

def buscar_resto(request):

    data = request.GET.get('nombre', "")
    error = ""

    if data: 

        resto = Restaurante.objects.filter(nombre=data)
        return render(request, 'app_final/formulario_buscar_resto.html', {"resto": resto, "id": data})

    return render(request, 'app_final/formulario_buscar_resto.html', {"error": error})