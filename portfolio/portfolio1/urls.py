from django.urls import path

from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse_lazy
from portfolio1 import views
from django.contrib.auth.views import LogoutView




urlpatterns = [

#----->Inicio<------ 

    path('', views.inicio, name="Inicio"),

#---->Admin<----

    path('admin/', admin.site.urls),
    # path('admin', views.admin, name="admin"),

#----->REGISTRO LOGIN EDIT USER<------
    
    path('login', views.login_request, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('editarUser', views.editarUser, name='EditarUser'),

#----->Yo<------ 

    path('yo', views.yo, name="Yo"),

    #path('yoBuscar', views.yoBuscar, name="yoBuscar"),
    path(r'^nuevo$', views.YoNuevo.as_view(), name='yoNuevo'),
    path(r'^editar/(?P<pk>\d+)$', views.YoUpdate.as_view(), name='yoEditar'),
    path(r'^borrar/(?P<pk>\d+)$', views.YoDelete.as_view(), name='yoEliminar'),
    #path(r'^(?P<pk>\d+)$', views.YoDetalle.as_view(), name='yoDetalle'),
    path('yoListar', views.YoList.as_view(), name='yoListar'),


#----->Skills<------ 

    path('skills_educacion', views.skills, name="Skills"),

#----->HardSkills<------ 

    #path('hardSkillsBuscar', views.hardSkillsBuscar, name="hardSkillsBuscar"),
    path(r'^nuevoh$', views.HardSkillsNuevo.as_view(), name='hardSkillsNuevo'),
    path(r'^editarh/(?P<pk>\d+)$', views.HardSkillsUpdate.as_view(), name='hardSkillsEditar'),
    path(r'^borrarh/(?P<pk>\d+)$', views.HardSkillsDelete.as_view(), name='hardSkillsEliminar'),
    #path(r'^(?P<pk>\d+)$', views.HardSkillsDetalle.as_view(), name='hardSkillsDetalle'),
    path('hardSkillsListar', views.HardSkillsList.as_view(), name='hardSkillsListar'),

# #----->SoftSkills<------ 
    
    #path('softSkillsBuscar', views.softSkillsBuscar, name="softSkillsBuscar"),
    path(r'^nuevos$', views.SoftSkillsNuevo.as_view(), name='softSkillsNuevo'),
    path(r'^editars/(?P<pk>\d+)$', views.SoftSkillsUpdate.as_view(), name='softSkillsEditar'),
    path(r'^borrars/(?P<pk>\d+)$', views.SoftSkillsDelete.as_view(), name='softSkillsEliminar'),
    #path(r'^(?P<pk>\d+)$', views.SoftSkillsDetalle.as_view(), name='softSkillsDetalle'),
    path('softSkillsListar', views.SoftSkillsList.as_view(), name='softSkillsListar'),

#----->Educación<------ 

    path('skills_educacion', views.educacionFunc, name="Educacion"),

    #path('educacionBuscar', views.educacionBuscar, name="educacionBuscar"),
    path(r'^nuevoe$', views.EducacionNuevo.as_view(), name='educacionNuevo'),
    path(r'^editare/(?P<pk>\d+)$', views.EducacionUpdate.as_view(), name='educacionEditar'),
    path(r'^borrare/(?P<pk>\d+)$', views.EducacionDelete.as_view(), name='educacionEliminar'),
    #path(r'^(?P<pk>\d+)$', views.EducacionDetalle.as_view(), name='educacionDetalle'),
    path('educacionListar', views.EducacionList.as_view(), name='educacionListar'),

#----->Experiencia Profesional<------ 

    path('skills_educacion', views.expProfesionalFunc, name="ExpProfesional"),

    #path('expProfesionalBuscar', views.expProfesionalBuscar, name="expProfesionalBuscar"),
    path(r'^nuevop$', views.ExpProfesionalNuevo.as_view(), name='expProfesionalNuevo'),
    path(r'^editarp/(?P<pk>\d+)$', views.ExpProfesionalUpdate.as_view(), name='expProfesionalEditar'),
    path(r'^borrarp/(?P<pk>\d+)$', views.ExpProfesionalDelete.as_view(), name='expProfesionalEliminar'),
    #path(r'^(?P<pk>\d+)$', views.ExpProfesionalDetalle.as_view(), name='expProfesionalDetalle'),
    path('expProfesionalListar', views.ExpProfesionalList.as_view(), name='expProfesionalListar'),

#----->Proyectos<------ 

    path('proyectos_intereses', views.proyectosFunc, name="Proyectos"),

    #path('proyectosBuscar', views.proyectosBuscar, name="proyectosBuscar"),
    path(r'^nuevoy$', views.ProyectosNuevo.as_view(), name='proyectosNuevo'),
    path(r'^editary/(?P<pk>\d+)$', views.ProyectosUpdate.as_view(), name='proyectosEditar'),
    path(r'^borrary/(?P<pk>\d+)$', views.ProyectosDelete.as_view(), name='proyectosEliminar'),
    path(r'^(?P<pk>\d+)$', views.ProyectosDetalle.as_view(), name='proyectosDetalle'),
    path('proyectosListar', views.ProyectosList.as_view(), name='proyectosListar'),

#----->Intereses<------ 

    path('proyectos_intereses', views.interesesFunc, name="Intereses"),

    #path('interesesBuscar', views.interesesBuscar, name="interesesBuscar"),
    path(r'^nuevoi$', views.InteresesNuevo.as_view(), name='interesesNuevo'),
    path(r'^editari/(?P<pk>\d+)$', views.InteresesUpdate.as_view(), name='interesesEditar'),
    path(r'^borrari/(?P<pk>\d+)$', views.InteresesDelete.as_view(), name='interesesEliminar'),
    #path(r'^(?P<pk>\d+)$', views.InteresesDetalle.as_view(), name='interesesDetalle'),
    path('interesesListar', views.InteresesList.as_view(), name='interesesListar'),
    
#----->Editar Portfolio<------ 

    path('superListar', views.superListarFunc, name="superListar"),

#----->Buscador<------ 

    path('buscador', views.buscadorFunc, name="buscador"),

]