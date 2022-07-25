from typing import List
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from portfolio1.models import Yo, HardSkills, SoftSkills, Educacion, ExpProfesional, Proyectos, Intereses
from portfolio1.forms import YoFormulario, HardSkillsFormulario, SoftSkillsFormulario, EducacionFormulario, ExpProfesionalFormulario, ProyectosFormulario, InteresesFormulario, UserRegisterForm, UserEditForm

from django.db.models import Q

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



#---> Admin <---

# def admin(request):
     
#       return render(request, "admin")

#---> Inicio <---      

def inicio(request):
      
      
      if Yo.objects.get(id="1"):
            yo = Yo.objects.get(id="1")
            yo_slice = str(yo.imagen)[11:]
           
            return render(request, "portfolio1/inicio.html",{"yo":yo, "yo_slice":yo_slice})
      else:
            return render(request, "portfolio1/inicio.html")

#----->Editar Portfolio<------ 
@login_required
def superListarFunc(request):
      yo = Yo.objects.all()
      hard_skills = HardSkills.objects.all()
      soft_skills = SoftSkills.objects.all()
      educacion = Educacion.objects.all()
      expProfesional = ExpProfesional.objects.all()
      intereses = Intereses.objects.all()
      proyectos = Proyectos.objects.all()
      usuario = request.user
      
      return render(request, "portfolio1/superListar.html",{"educacion":educacion, "expProfesional":expProfesional, "soft_skills":soft_skills, "hard_skills":hard_skills, "intereses":intereses, "proyectos":proyectos, "yo":yo, "usuario":usuario})

  

#---> Yo <---

def yo(request):
      yo = Yo.objects.get(id="1")
      yo_slice = str(yo.imagen)[11:]
      return render(request, "portfolio1/yo.html",{"yo":yo, "yo_slice":yo_slice})


class YoNuevo(CreateView):

      model = Yo
      success_url = reverse_lazy(inicio)
      fields = ['nombre', 'apellido','telefono','email','fechaDeNacimiento','webSite','ciudad','disponibilidad', 'palabrasClave', 'resumen', 'imagen']

class YoUpdate(UpdateView):

      model = Yo
      success_url = reverse_lazy(superListarFunc)
      fields  = ['nombre', 'apellido','telefono','email','fechaDeNacimiento','webSite','ciudad','disponibilidad', 'palabrasClave', 'resumen', 'imagen']

class YoDelete(DeleteView):

      model = Yo
      success_url = reverse_lazy(superListarFunc)

class YoList(ListView):

      model = Yo 
      template_name = "portfolio1/yo_list.html"

class YoDetalle(DetailView):

      model = Yo
      template_name = "portfolio1/yo_detail.html"

#---> Skills <---

def skills(request):
      hard_skills = HardSkills.objects.all()
      soft_skills = SoftSkills.objects.all()

      educacion = Educacion.objects.all()

      expProfesional = ExpProfesional.objects.all()

      yo = Yo.objects.get(id="1")
      yo_slice = str(yo.imagen)[11:]
      return render(request, "portfolio1/skills_educacion.html",{"hard_skills":hard_skills, "soft_skills":soft_skills, "educacion":educacion, "expProfesional":expProfesional, "yo":yo, "yo_slice":yo_slice})


#---> Hard Skills <---

class HardSkillsNuevo(CreateView):

      model = HardSkills
      success_url = reverse_lazy(superListarFunc)
      fields = ['hardSkills', 'porcentaje']

class HardSkillsUpdate(UpdateView):

      model = HardSkills
      success_url = reverse_lazy(superListarFunc)
      fields  = ['hardSkills', 'porcentaje']

      
class HardSkillsDelete(DeleteView):

      model = HardSkills
      success_url = reverse_lazy(superListarFunc)

class HardSkillsList(ListView):

      model = HardSkills 
      template_name = "portfolio1/hardSkills_list.html"


#---> Soft Skills <---

class SoftSkillsNuevo(CreateView):

      model = SoftSkills
      success_url =  reverse_lazy(superListarFunc)
      fields = ['softSkills', 'porcentaje']

class SoftSkillsUpdate(UpdateView):

      model = SoftSkills
      success_url = reverse_lazy(superListarFunc)
      fields  = ['softSkills', 'porcentaje']

      
class SoftSkillsDelete(DeleteView):

      model = SoftSkills
      success_url = reverse_lazy(superListarFunc)

class SoftSkillsList(ListView):

      model = SoftSkills 
      template_name = "portfolio1/softSkills_list.html"


#---> Educación <---

def educacionFunc(request):
      educacion = Educacion.objects.all()
      
      hard_skills = HardSkills.objects.all()
      soft_skills = SoftSkills.objects.all()

      expProfesional = ExpProfesional.objects.all()
      
      yo = Yo.objects.get(id="1")
      yo_slice = str(yo.imagen)[11:]
      
      return render(request, "portfolio1/skills_educacion.html",{"educacion":educacion, "hard_skills":hard_skills, "soft_skills":soft_skills, "expProfesional":expProfesional, "yo":yo, "yo_slice":yo_slice})



class EducacionNuevo(CreateView):

      model = Educacion
      success_url = reverse_lazy(superListarFunc)
      fields  = ['titulo', 'fechaIni', 'fechaFin', 'lugar', 'ciudad', 'resumen', 'status']

class EducacionUpdate(UpdateView):

      model = Educacion
      success_url = reverse_lazy(superListarFunc)
      fields  = ['titulo', 'fechaIni', 'fechaFin', 'lugar', 'ciudad', 'resumen', 'status']

      
class EducacionDelete(DeleteView):

      model = Educacion
      success_url = reverse_lazy(superListarFunc)

class EducacionList(ListView):

      model = Educacion 
      template_name = "portfolio1/educacion_list.html"


#---> Experiencia Profesional <---

def expProfesionalFunc(request):
      expProfesional = ExpProfesional.objects.all()
      
      hard_skills = HardSkills.objects.all()
      soft_skills = SoftSkills.objects.all()

      educacion = Educacion.objects.all()
      
      yo = Yo.objects.get(id="1")
      yo_slice = str(yo.imagen)[11:]
      
      return render(request, "portfolio1/skills_educacion.html",{"expProfesional":expProfesional, "educacion":educacion, "hard_skills":hard_skills, "soft_skills":soft_skills, "yo":yo, "yo_slice":yo_slice})



class ExpProfesionalNuevo(CreateView):

      model = ExpProfesional
      success_url = reverse_lazy(superListarFunc)
      fields  = ['titulo', 'fechaIni', 'fechaFin', 'lugar', 'ciudad', 'resumen']



class ExpProfesionalUpdate(UpdateView):

      model = ExpProfesional
      success_url = reverse_lazy(superListarFunc)
      fields  = ['titulo', 'fechaIni', 'fechaFin', 'lugar', 'ciudad', 'resumen']

      
class ExpProfesionalDelete(DeleteView):

      model = ExpProfesional
      success_url = reverse_lazy(superListarFunc)

class ExpProfesionalList(ListView):

      model = ExpProfesional 
      template_name = "portfolio1/expProfesional_list.html"

#---> Proyectos <---

def proyectosFunc(request):
      proyectos = Proyectos.objects.all()
      
      intereses = Intereses.objects.all()
      
      yo = Yo.objects.get(id="1")
      yo_slice = str(yo.imagen)[11:]

      print("entro al if")
            
      count = 0
      for proy in proyectos:
            count += 1
            #recorro por id el modelo. While try por si falta un ID.
            w = False
            while w == False:
                  try:
                        proyectos = Proyectos.objects.get(id=count)
                        w = True
                        

                  except:
                        print(f"Falta el ID: {count}")
                        count += 1

            starts = str(proy.imagen)
            if starts.startswith("portfolio1/") == True:
                  proyectos = Proyectos.objects.get(id=count)
                  proyectos.imagen = str(proy.imagen)[11:]
                  proyectos.save()
                  
                  
                  
      proyectos = Proyectos.objects.all()
      return render(request, "portfolio1/proyectos_intereses.html",{"proyectos":proyectos, "intereses":intereses, "yo":yo, "yo_slice":yo_slice})



class ProyectosNuevo(CreateView):

      model = Proyectos
      success_url = reverse_lazy(superListarFunc)
      fields  = ['titulo', 'contenido', 'imagen', 'creado']

class ProyectosUpdate(UpdateView):

      model = Proyectos
      success_url = reverse_lazy(superListarFunc)
      fields  = ['titulo', 'contenido', 'imagen', 'creado']

      
class ProyectosDelete(DeleteView):

      model = Proyectos
      success_url = reverse_lazy(superListarFunc)

class ProyectosList(ListView):

      model = Proyectos 
      template_name = "portfolio1/proyectos_list.html"

class ProyectosDetalle(DetailView):

      model = Proyectos
      template_name = "portfolio1/proyectos_detail.html"

#---> Intereses <---

def interesesFunc(request):
      intereses = Intereses.objects.all()
      
      proyectos = Proyectos.objects.all()
      
      yo = Yo.objects.get(id="1")
      yo_slice = str(yo.imagen)[11:]

     
      count = 0
      for proy in proyectos:
            count += 1
            starts = str(proy.imagen)
            if starts.startswith("portfolio1/") == True:
                  proyectos = Proyectos.objects.get(id=count)
                  proyectos.imagen = str(proy.imagen)[11:]
                  proyectos.save()
      proyectos = Proyectos.objects.all()
      return render(request, "portfolio1/proyectos_intereses.html",{"intereses":intereses, "proyectos":proyectos,  "yo":yo, "yo_slice":yo_slice})



class InteresesNuevo(CreateView):

      model = Intereses
      success_url = reverse_lazy(superListarFunc)
      fields  = ['titulo', 'resumen']

class InteresesUpdate(UpdateView):

      model = Intereses
      success_url = reverse_lazy(superListarFunc)
      fields  = ['titulo', 'resumen']

      
class InteresesDelete(DeleteView):

      model = Intereses
      success_url = reverse_lazy(superListarFunc)

class InteresesList(ListView):

      model = Intereses 
      template_name = "portfolio1/intereses_list.html"


    

#----->Editar Portfolio<------

def buscadorFunc(request):
      educacion_t = False
      expProfesional_t = False
      hard_skills_t = False
      soft_skills_t = False
      proyectos_t = False
      intereses_t = False
      
      if request.method == "POST":

        
        search = request.POST["search"]

        if search != "":

            educacionb = Educacion.objects.filter( Q(titulo__icontains=search) | Q(lugar__icontains=search) | Q(ciudad__icontains=search) ).values()
            if Educacion.objects.filter( Q(titulo__icontains=search) | Q(lugar__icontains=search) | Q(ciudad__icontains=search) ).values():
                  educacion_t = True

            expProfesionalb = ExpProfesional.objects.filter( Q(titulo__icontains=search) | Q(lugar__icontains=search) | Q(ciudad__icontains=search) ).values()
            if ExpProfesional.objects.filter( Q(titulo__icontains=search) | Q(lugar__icontains=search) | Q(ciudad__icontains=search) ).values():
                  expProfesional_t = True

            hard_skillsb = HardSkills.objects.filter( Q( hardSkills__icontains=search) ).values()
            if HardSkills.objects.filter( Q( hardSkills__icontains=search) ).values():
                  hard_skills_t = True

            soft_skillsb = SoftSkills.objects.filter( Q( softSkills__icontains=search) ).values()
            if SoftSkills.objects.filter( Q( softSkills__icontains=search) ).values():
                  soft_skills_t = True

            proyectosb = Proyectos.objects.filter( Q( titulo__icontains=search) | Q(contenido__icontains=search) | Q(creado__icontains=search) ).values()
            if Proyectos.objects.filter( Q( titulo__icontains=search) | Q(contenido__icontains=search) | Q(creado__icontains=search) ).values():
                  proyectos_t = True

            interesesb = Intereses.objects.filter( Q( titulo__icontains=search) | Q(resumen__icontains=search) ).values()
            if Intereses.objects.filter( Q( titulo__icontains=search) | Q(resumen__icontains=search) ).values():
                  intereses_t = True
                  
            
            return render(request, "portfolio1/buscador.html",{"educacion_t":educacion_t, "expProfesional_t":expProfesional_t, "hard_skills_t":hard_skills_t, "soft_skills_t":soft_skills_t, "proyectos_t":proyectos_t, "intereses_t":intereses_t, "educacionb":educacionb, "expProfesionalb":expProfesionalb, "soft_skillsb":soft_skillsb, "hard_skillsb":hard_skillsb, "interesesb":interesesb, "proyectosb":proyectosb, "search":True, "busqueda":search})

        else:
            no_dato = "No se ingresaron datos. "
            return render(request, "portfolio1/buscador.html", {"no_dato":no_dato})

      return render(request, "portfolio1/buscador.html")


#----->REGISTRO LOGIN EDIT USER<------


def login_request(request):
      
      yo = Yo.objects.get(id="1")
      yo_slice = str(yo.imagen)[11:]
      
      if request.method == "POST":
            
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contrasenia = form.cleaned_data.get('password')
                  user = authenticate(username = usuario , password = contrasenia)
                  
                  if user is not None:
                        login(request, user)
                        return inicio(request)
                       
                  else:
                        print("Arafue")
                        return render(request, "portfolio1/login.html", {"mensaje":"Datos invalidos", 'form': form, "yo":yo, "yo_slice":yo_slice})
            else:
                  print("no valido")
                  return render(request, "portfolio1/login.html", {"mensaje":"Datos invalidos", 'form': form, "yo":yo, "yo_slice":yo_slice})

      
      
      form = AuthenticationForm()
      
      return render(request, "portfolio1/login.html", {'form': form, "yo":yo, "yo_slice":yo_slice})



def register(request):

      yo = Yo.objects.get(id="1")
      yo_slice = str(yo.imagen)[11:]
         
      if request.method == "POST":
            
            form = UserRegisterForm(request.POST)

            if form.is_valid():
                  
                  username = form.cleaned_data['username']
                 
                  form.save()
                  print('lo vamo a inicio')
                  return inicio(request)
      else:
            print("no es valido formulario")
            form = UserRegisterForm()
      print("Llegue")
      return render(request, "portfolio1/registro.html", {'form': form, "yo":yo, "yo_slice":yo_slice})



@login_required
def editarUser(request):

      yo = Yo.objects.get(id="1")
      yo_slice = str(yo.imagen)[11:]

      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid(): 
                  informacion = miFormulario.cleaned_data
                  
                  
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.save()
                  print("Llamo superListar")
                  return superListarFunc(request)

      else:
            print("aca se rompe")
            miFormulario = UserEditForm(initial={'email':usuario.email})
      
      
      return render(request, "portfolio1/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario, "yo":yo, "yo_slice":yo_slice})


def logout_view(request):
    logout(request)
    return inicio(request)
    