from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label=_('Correo electrónico')) 

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': _('Nombre de usuario'),  
            'password1': _('Contraseña'), 
            'password2': _('Confirmar contraseña'),  
        }
        help_texts = {
            'password1': _('La contraseña debe contener al menos 8 caracteres.'),  
            'password2': _('Ingresa la misma contraseña que arriba, para verificar.'),  
        }
        error_messages = {
            'password2': {
                'password_mismatch': _('Las contraseñas no coinciden.'),  
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].error_messages = {
            'password_too_short': _('La contraseña es demasiado corta.'),
            'password_too_common': _('La contraseña es muy común.'),
            'password_entirely_numeric': _('La contraseña no puede ser totalmente numérica.'),
            'password_similar_to_username': _('La contraseña no puede ser demasiado similar a tu nombre de usuario.')
        }
