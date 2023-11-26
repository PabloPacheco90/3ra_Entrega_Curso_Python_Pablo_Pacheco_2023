from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    filter_horizontal = ('groups', 'user_permissions')  # Para mostrar las relaciones ManyToManyField de forma más amigable
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

# Registra el modelo CustomUser y aplica la personalización del admin
admin.site.register(CustomUser, CustomUserAdmin)
