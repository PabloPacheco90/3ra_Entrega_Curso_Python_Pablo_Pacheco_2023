from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import EmpleadoForm,DepartamentoForm,PlantaForm
from .models import Empleado,Departamento,Planta
from .forms import BuscarForm

@login_required
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

@login_required
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

@login_required
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


def eliminar_planta(request, planta_id):
    if request.user.is_authenticated:
        planta = get_object_or_404(Planta, pk=planta_id)
        planta.delete()
        return redirect('listar_plantas') 
    else:
        return render(request, 'mensaje_no_autenticado.html')
    

def eliminar_empleado(request, empleado_id):
    if request.user.is_authenticated:
        empleado = get_object_or_404(Empleado, pk=empleado_id)

        empleado.delete()
        return redirect('listar_empleados')  
    else:
        return render(request, 'mensaje_no_autenticado.html')
    
def eliminar_departamento(request, departamento_id):
    if request.user.is_authenticated:
        departamento = get_object_or_404(Departamento, pk=departamento_id)
        departamento.delete()
        return redirect('listar_departamentos')  
    else:
        return render(request, 'mensaje_no_autenticado.html')    