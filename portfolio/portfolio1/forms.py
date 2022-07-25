from django import forms

from dataclasses import fields

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#------>USER FORMS <------

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Password:', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Password confirmation:', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm): 
    

    email = forms.EmailField(label='modificar email')
    password1 = forms.CharField(label='Password:', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Password confirmation:', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}




#------> FORMS <------

class YoFormulario(forms.Form):
    nombre= forms.CharField(max_length=30, label= "Nombre")
    apellido= forms.CharField(max_length=30, label= "Apellido")
    telefono = forms.IntegerField(label= "Teléfono")
    email= forms.EmailField(label= "Email")
    fechaDeNacimiento = forms.DateField(label= "Nacimiento")
    webSite = forms.CharField(max_length=55, label= "Website")
    ciudad = forms.CharField(max_length=30, label= "ciudad")
    disponibilidad = forms.BooleanField(label= "Disponibilidad")
    palabrasClave =  forms.CharField(max_length=300, label="Palabras Clave")
    resumen =  forms.CharField(max_length=300, label="Resumen")
    imagen = forms.ImageField(label="Imagen")

    

class HardSkillsFormulario(forms.Form):
    hardSkills = forms.CharField(max_length=50,label="Habilidad")
    porcentaje = forms.IntegerField(label="Porcentaje")

   
class SoftSkillsFormulario(forms.Form):
    softSkills = forms.CharField(max_length=50,label="Habilidad")
    porcentaje = forms.IntegerField()


class EducacionFormulario(forms.Form):
    titulo = forms.CharField(max_length=50, label="Título")
    fechaIni = forms.DateTimeField(label="Fecha de Inicio")
    fechaFin = forms.DateTimeField(label="Fecha de Finalización")
    lugar = forms.CharField(max_length=50, label="Lugar")
    ciudad = forms.CharField(max_length=30, label= "ciudad")
    resumen = forms.CharField(max_length=240, label="Resumen")
    status = forms.CharField(max_length=30, label="Status")

   

class ExpProfesionalFormulario(forms.Form):
    titulo = forms.CharField(max_length=50, label="Título")
    fechaIni = forms.DateTimeField(label="Fecha de Inicio")
    fechaFin = forms.DateTimeField(label="Fecha de Finalización")
    lugar = forms.CharField(max_length=50, label="Lugar")
    ciudad = forms.CharField(max_length=30, label= "ciudad")
    resumen = forms.CharField(max_length=240, label="Resumen")
   
   

class ProyectosFormulario(forms.Form):
    titulo = forms.CharField(max_length=240, label="Título")
    contenido = forms.CharField(max_length=300, label="Contenido")
    imagen = forms.ImageField(label="Imagen")
    creado = forms.DateField(label="Fecha de creación")
  

class InteresesFormulario(forms.Form):
    titulo = forms.CharField(max_length=50, label="Intereses")
    resumen = forms.CharField(max_length=240, label="Resumen")

  