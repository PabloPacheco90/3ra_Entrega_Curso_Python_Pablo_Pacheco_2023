# forms.py
from django import forms
from .models import Empleado,Departamento,Planta

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'edad','profesion']  # Lista los campos que deseas incluir en el formulario

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre', 'modalidad_trabajo', 'sueldo_promedio']        

class PlantaForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = ['nombre', 'localidad', 'provincia']

class BuscarForm(forms.Form):
    termino_busqueda = forms.CharField(label='Buscar')       