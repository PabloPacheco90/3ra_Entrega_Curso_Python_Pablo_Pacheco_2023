from django.shortcuts import render, redirect
from .forms import EmpleadoForm,DepartamentoForm,PlantaForm
from .models import Empleado,Departamento,Planta

def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_principal')

    else:
        form = EmpleadoForm()

    return render(request, 'agregar_empleado.html', {'form': form})

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'lista_empleados.html', {'empleados': empleados})

def agregar_departamento(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_principal') 
    else:
        form = DepartamentoForm()

    return render(request, 'agregar_departamento.html', {'form': form})

def listar_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'lista_departamentos.html', {'departamentos': departamentos})

def agregar_planta(request):
    if request.method == 'POST':
        form = PlantaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_principal')
    else:
        form = PlantaForm()

    return render(request, 'agregar_planta.html', {'form': form})

def listar_plantas(request):
    plantas = Planta.objects.all()
    return render(request, 'lista_planta.html', {'plantas': plantas})

from django.shortcuts import render
from .forms import BuscarForm
from .models import Empleado, Departamento, Planta

def buscar(request):
    form = BuscarForm(request.GET)
    resultados = []

    if form.is_valid():
        termino_busqueda = form.cleaned_data['termino_busqueda']

        # Realiza la búsqueda en los modelos que desees
        empleados = Empleado.objects.filter(nombre__icontains=termino_busqueda)
        departamentos = Departamento.objects.filter(nombre__icontains=termino_busqueda)
        plantas = Planta.objects.filter(nombre__icontains=termino_busqueda)

        # Agrega los resultados a la lista
        resultados.extend(empleados)
        resultados.extend(departamentos)
        resultados.extend(plantas)

    return render(request, 'buscar_resultados.html', {'form': form, 'resultados': resultados})

from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def contacto(request):
    return render(request, 'contacto.html')