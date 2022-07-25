from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth.models import User

class Yo(models.Model):
    nombre= models.CharField(max_length=30, verbose_name="Nombre")
    apellido= models.CharField(max_length=30, verbose_name="Apellido")
    telefono = models.IntegerField(verbose_name="Teléfono")
    email= models.EmailField(verbose_name="E-mail")
    fechaDeNacimiento = models.DateField(verbose_name="Nacimiento")
    webSite = models.CharField(max_length=55, verbose_name="Website")
    ciudad = models.CharField(max_length=30, verbose_name="Ciudad")
    disponibilidad = models.BooleanField(verbose_name="Disponibilidad")
    palabrasClave =  models.CharField(max_length=300, verbose_name="Palabras Clave")
    resumen =  models.CharField(max_length=300, verbose_name="Resumen")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="portfolio1/static/assets/img", null=True, blank=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - Teléfono {self.telefono} - E-Mail {self.email} - Fecha De Nacimiento {self.fechaDeNacimiento} - Web Site {self.webSite} - Ciudad {self.ciudad} - Disponibilidad {self.disponibilidad} - Resumen {self.resumen} - Palabras clave {self.palabrasClave} - Imagen {self.imagen}"


class HardSkills(models.Model):
    hardSkills = models.CharField(max_length=50, verbose_name="Habilidad")
    porcentaje = models.IntegerField(choices=list(zip(range(1, 101), range(1, 101))), unique=True)

    def __str__(self):
        return f"HardSkills: {self.hardSkills} - Porcentaje {self.porcentaje}"

class SoftSkills(models.Model):
    softSkills = models.CharField(max_length=50, verbose_name="Habilidad")
    porcentaje = models.IntegerField(choices=list(zip(range(1, 101), range(1, 101))), unique=True)

    def __str__(self):
        return f"SoftSkills: {self.softSkills} - Porcentaje {self.porcentaje}"


class Educacion(models.Model):
    titulo = models.CharField(max_length=50, verbose_name="Título")
    fechaIni = models.DateField(verbose_name="Fecha de Inicio")
    fechaFin = models.DateField(verbose_name="Fecha de Finalización")
    lugar = models.CharField(max_length=50, verbose_name="Lugar")
    ciudad = models.CharField(max_length=30, verbose_name="Ciudad")
    resumen = models.CharField(max_length=240, verbose_name="Resumen")
    STATUSES = [
        ('Completo', 'Completo'),
        ('Incompleto', 'Incompleto'),
        ('Cursando', 'Cursando'),
        ('En Pausa', 'En Pausa')
        ]
    status = models.CharField(max_length=30, choices=STATUSES, verbose_name="Status")
    
    def __str__(self):
        return f"Título: {self.titulo} - Fecha de Inicio {self.fechaIni} - Fecha de Finalización {self.fechaFin} - Lugar {self.lugar} - Ciudad {self.ciudad} - Resumen {self.resumen} - Status {self.status}"


class ExpProfesional(models.Model):
    titulo = models.CharField(max_length=50, verbose_name="Título")
    fechaIni = models.DateField(verbose_name="Fecha de Inicio")
    fechaFin = models.DateField(verbose_name="Fecha de Finalización")
    lugar = models.CharField(max_length=50, verbose_name="Lugar")
    ciudad = models.CharField(max_length=30, verbose_name="Ciudad")
    resumen = models.CharField(max_length=240, verbose_name="Resumen")
   
    def __str__(self):
        return f"Título: {self.titulo} - Fecha de Inicio {self.fechaIni} - Fecha de Finalización{self.fechaFin} - Lugar {self.lugar} - Ciudad {self.ciudad} - Resumen {self.resumen}"



class Proyectos(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    contenido = models.TextField(max_length=240, verbose_name="Contenido")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="portfolio1/static/assets/img", null=True, blank=True)
    creado = models.DateField(verbose_name="Fecha de creación")
     
    def __str__(self):
        return f"Título: {self.titulo} - Contenido: {self.contenido} - Imagen: {self.imagen} - Fecha de Creación: {self.creado}"


class Intereses(models.Model):
    titulo = models.CharField(max_length=50, verbose_name="Intereses")
    resumen = models.CharField(max_length=240, verbose_name="Resumen")

    def __str__(self):
        return f"Título: {self.titulo} - Resumen: {self.resumen}"