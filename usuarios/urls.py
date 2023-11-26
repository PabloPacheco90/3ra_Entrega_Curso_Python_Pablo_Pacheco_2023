from django.urls import path
from usuarios.views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('principal/', pagina_principal, name='principal'),
    path('profile/', profile_view, name='profile'),
    path('login/', user_login, name='login'),
    path('logout/', cerrar_sesion, name='logout'),

    
]
