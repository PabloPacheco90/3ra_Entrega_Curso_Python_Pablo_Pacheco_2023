# urls.py

from django.urls import path
from .views import (
    agregar_empleado, lista_empleados,
    agregar_departamento, listar_departamentos,
    agregar_planta, listar_plantas,buscar
,inicio,contacto)

urlpatterns = [
    

    path('inicio/', inicio, name='inicio'),
    path('contacto/', contacto, name='contacto'),

    # URL para agregar y listar empleados
    path('agregar_empleado/', agregar_empleado, name='agregar_empleado'),
    path('lista_empleados/', lista_empleados, name='listar_empleados'),

    # URL para agregar y listar departamentos
    path('agregar_departamento/', agregar_departamento, name='agregar_departamento'),
    path('lista_departamentos/', listar_departamentos, name='listar_departamentos'),

    # URL para agregar y listar plantas
    path('agregar_planta/', agregar_planta, name='agregar_planta'),
    path('lista_plantas/', listar_plantas, name='listar_plantas'),
    path('buscar/', buscar, name='buscar'),
]
    # Otras URL...
