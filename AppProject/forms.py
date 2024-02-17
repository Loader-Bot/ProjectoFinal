from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import re
from AppProject.models import NewsPost


def validate_password(value):
    if re.match(r'^[0-9]+$', value):
        raise ValidationError('La contraseña no puede ser solo números.')
    if not re.match(r'^[a-zA-Z0-9]+$', value):
        raise ValidationError('La contraseña no puede contener caracteres especiales.')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Nombre de Usuario', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=15, required=True, help_text='Requerido. Máximo 15 caracteres. Solo letras, números y @/./+/-/_ permitidos.')
    first_name = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=30, help_text='Requerido. Ingresa tu nombre')
    last_name = forms.CharField(label='Apellido',widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=30, help_text='Requerido. Ingresa tu apellido.')
    email = forms.EmailField(max_length=254,widget=forms.TextInput(attrs={'class': 'form-control'}), help_text='Requerido. Ingresa tu correo electrónico.')
    password1 = forms.CharField(label="Contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[validate_password],
        help_text='Requerido. La contraseña no puede ser solo números y no debe contener caracteres especiales.')

    password2 = forms.CharField(label="Confirmar Contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[validate_password],
        help_text='Requerido. Ingresa la misma contraseña que antes para verificarla.')
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden.")
        return password2

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, help_text='Ingresa tu nombre')
    last_name = forms.CharField(max_length=30, help_text='Ingresa tu apellido.')
    email = forms.EmailField(max_length=254, help_text='Ingresa tu correo electrónico.')
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','password1','password2']   

class AvatarForm(forms.Form):
    image = forms.ImageField()     

class PostForm(forms.ModelForm):
    class Meta:
        model = NewsPost
        fields = ['title', 'subtitle', 'content', 'image']        