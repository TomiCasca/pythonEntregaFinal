from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from usuarios.models import Perfil

class CrearUsuario(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmación de contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # help_texts = {
        #     'username': '',
        #     'email': '',
        #     ...
        # }
        help_texts = {key: '' for key in fields}
    
        
class EditarPerfil(forms.ModelForm):
    
    class Meta:
        model = Perfil
        fields = ['fecha_nacimiento', 'biografia', 'avatar']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})
        }