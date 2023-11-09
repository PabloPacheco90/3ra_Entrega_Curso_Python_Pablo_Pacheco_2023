from django.shortcuts import render

def pagina_principal(request):
    # Lógica de la vista
    return render(request, 'principal.html')