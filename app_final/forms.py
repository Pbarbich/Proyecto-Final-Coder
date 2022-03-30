from django import forms

class Formulario_resto(forms.Form):

    #Campos del formulario
    nombre = forms.CharField(max_length = 40)
    mail = forms.EmailField(max_length = 40)
    comida = forms.CharField(max_length = 40)
    direccion = forms.CharField(max_length = 60)

class Formulario_plataformas(forms.Form):

    #Campos del formulario
    empresa = forms.CharField(max_length = 40)
    mail = forms.EmailField(max_length = 40)

class Formulario_menu(forms.Form):

    #Campos del formulario
    nombre =  forms.CharField(max_length = 40)
    descripcion = forms.CharField(max_length = 100)
    precio = forms.IntegerField()

class Formulario_clientes(forms.Form):

    #Campos del formulario
    nombre = forms.CharField(max_length = 40)
    mail = forms.EmailField()
    celular = forms.IntegerField()