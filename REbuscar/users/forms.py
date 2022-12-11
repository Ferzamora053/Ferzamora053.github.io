from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(required=True, label='Nombre de usuario' )
    password1 = forms.CharField(required=True, widget=forms.PasswordInput, label='Contraseña')
    password2 = forms.CharField(required=True, widget=forms.PasswordInput, label='Repita su contraseña')
    email = forms.EmailField(required=True, label='Dirección de correo electrónico')
    name = forms.CharField(required=True, label='Nombre')
    
    class Meta:
        model = User
        fields = [
            'name', 
            'email', 
            'username', 
            'password1', 
            'password2',
        ]