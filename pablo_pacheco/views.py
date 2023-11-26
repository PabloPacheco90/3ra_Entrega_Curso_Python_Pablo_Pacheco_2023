from django.shortcuts import render

def pagina_principal(request):
    # Lógica de la vista
    return render(request, 'principal.html')


def inicio(request):
    return render(request, 'inicio.html')

def about(request):
    return render(request, 'about.html')