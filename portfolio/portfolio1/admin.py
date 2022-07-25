from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
#registramos los modelos



admin.site.register(Yo)

admin.site.register(HardSkills)

admin.site.register(SoftSkills)

admin.site.register(Educacion)

admin.site.register(ExpProfesional)

admin.site.register(Proyectos)

admin.site.register(Intereses)
