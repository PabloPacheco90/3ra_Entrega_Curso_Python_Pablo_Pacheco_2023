from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Autenticar al usuario después del registro
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('principal')  # Reemplaza 'home' con el nombre de tu URL de página principal
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})
 
def pagina_principal(request):
    # Lógica de la vista
    return render(request, 'principal.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('principal')  # Reemplaza 'home' con el nombre de tu URL de página principal
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('pagina_principal')  

@login_required
def profile_view(request):
    user = request.user  # Obtener el usuario actualmente autenticado
    return render(request, 'profile.html', {'user': user})