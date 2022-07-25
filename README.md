# Proyecto-Final_Swidzinski-Sebastian-Python-Coderhouse

# Documentación Portfolio Web App

Este proyecto fue desarrollado en un entorno académico como cierre y entrega de un trabajo final del curso de Python con implementacón de Django en Coderhouse. Fue pensada para mostrar interactivamente CV y portfolio de un perfil previamente cargado. Todos los items son creados y almacenados en base a modelos. Estos pueden ser editados, eliminados, buscados y mostrados por medio del uso de la misma plataforma con login de user y password. La siguiente versión buscará poder operar con tantos perfiles como sean cargados y generar distintas URLs para cada perfil seleccionado.

# views.py

En éste módulo se encuentran las funciones y la lógica de nuestra aplicación. Recibirá y procesará información de los modelos y los "Submit" de las plantillas. Como así pasará los datos para renderizar una plantilla en respuesta. 
Las funciones superListarFunc y editarUser tienen el decorador @login_required.

# urls.py

Las solicitudes primero llegan a urls.py y luego van a la función de coincidencia en views.py.
templates
En este paquete se encuentran los templates en HTML, los cuales son consumidos por las distintas funciones de views.py. La mayoría de los templates heredan de padre.html, salvo superListar.html y buscador.html.

# models.py

En este módulo se especifíca la forma en que se organizan los datos en la db, según modelos. Estos datos son consumidos o guardados por las distintas funciones o "views" en views.py. Los módelos son: Yo, HardSkills, SoftSkills, Educación, ExpProfesional, Proyectos e Intereses

# forms.py

Aqui se encuentran los formularios basados en los modelos para ingreso y edición de datos de los distintos items.  Los distintos formularios son: UserRegisterForm (con Meta), UserEditForm (con Meta), YoFormulario, HardSkillsFormulario, SoftSkillsFormulario, EducacionFormulario, ExpProfesionalFormulario, ProyectosFormulario, InteresesFormulario


# Autor

Swidzinski Sebastián
