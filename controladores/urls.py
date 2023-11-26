# urls.py

from django.urls import path
from .views import (
    agregar_empleado, lista_empleados,
    agregar_departamento, listar_departamentos,
    agregar_planta, listar_plantas,buscar,eliminar_planta,eliminar_empleado,eliminar_departamento)

urlpatterns = [

    # URL para agregar y listar empleados
    path('agregar_empleado/', agregar_empleado, name='agregar_empleado'),
    path('lista_empleados/', lista_empleados, name='listar_empleados'),
    path('empleados/<int:empleado_id>/eliminar/', eliminar_empleado, name='eliminar_empleado'),


    # URL para agregar y listar departamentos
    path('agregar_departamento/', agregar_departamento, name='agregar_departamento'),
    path('lista_departamentos/', listar_departamentos, name='listar_departamentos'),
    path('departamentos/<int:departamento_id>/eliminar/', eliminar_departamento, name='eliminar_departamento'),


    # URL para agregar y listar plantas
    path('agregar_planta/', agregar_planta, name='agregar_planta'),
    path('lista_plantas/', listar_plantas, name='listar_plantas'),
    path('plantas/<int:planta_id>/eliminar/',eliminar_planta, name='eliminar_planta'),

    path('buscar/', buscar, name='buscar'),
]
  
