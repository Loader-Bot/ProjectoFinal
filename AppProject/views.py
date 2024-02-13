from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserEditForm, AvatarForm
from .models import *
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def registrar(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Autenticar al usuario después del registro
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                # Set URL Avatar to Sessión
                avatar = Avatar.objects.get_or_create(user=user)[0]

                if avatar.image:
                    request.session['avatar_url'] = avatar.image.url
    
                return render(request, 'index.html', {'form': form})
        else:
            messages.error(request, 'Datos incorrectos')
       
    else:
        form = UserRegistrationForm()

    return render(request, 'registrar_usuario.html', {'form': form})



def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirigir al perfil del usuario después de guardar los cambios
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'editar_usuario.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'index.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def avatar(request):
    if request.method == "POST":
        print("avatar - POST")
        formulario = AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():
            print("avatar - Is_Valid!")
            user = request.user

            avatar = Avatar.objects.filter(user=user).first()
            if avatar:
                avatar.delete()

            avatar = Avatar.objects.create(user=user, image=formulario.cleaned_data.get("image"))

            print("avatar - Success!")
            #messages.success(request, 'Imagen de perfil actualizada exitosamente.')

            # Set URL Avatar to Sessión
            avatar = Avatar.objects.get_or_create(user=user)[0]

            if avatar.image:
                request.session['avatar_url'] = avatar.image.url
  
            return redirect('index')


    formulario = AvatarForm()

    return render(request, 'avatar.html', {"form": formulario})
