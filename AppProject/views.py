from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserEditForm, AvatarForm, PostForm
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User




def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

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


@login_required
def editar_usuario(request):

    usuario = request.user
    if request.method == 'POST':
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario.first_name = informacion.get('first_name')
            usuario.last_name = informacion.get('last_name')
            usuario.email = informacion.get('email')
            usuario.password = informacion.get('password1')

            usuario.save()
            return render(request, 'index.html')
    formulario = UserEditForm(initial={'email': usuario.email})
    return render(request, 'editar_usuario.html', {'formulario' : formulario, 'usuario' : usuario})                              


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

@login_required
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

           
            # Set URL Avatar to Sessión
            avatar = Avatar.objects.get_or_create(user=user)[0]

            if avatar.image:
                request.session['avatar_url'] = avatar.image.url
  
            return redirect('index')


    formulario = AvatarForm()

    return render(request, 'avatar.html', {"form": formulario})

@login_required
def publicar_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            page = form.save(commit=False)
            page.author = request.user
            page.save()
            print('el post se guardo exitosamente')
            return redirect('index')
    else:
        form = PostForm()

    return render(request, 'publicar_post.html', {'form': form})    



def posts_list (request):
    pages = NewsPost.objects.all()
    return render(request, 'posts_list.html', {'pages': pages})

def post_detalles (request, pk):
    page = get_object_or_404(NewsPost, pk=pk)
    return render(request, 'post_detalles.html', {'page': page})


@login_required
def editar_post(request, pk):
    page = get_object_or_404(NewsPost, pk=pk, owner=request.user)
    if request.method == 'POST':
        form =PostForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm(instance=page)
    return render(request, 'editar_post.html', {'form': form})


@login_required
def borrar_post(request, pk):
    page = get_object_or_404(NewsPost, pk=pk, owner=request.user)
    if request.method == 'POST':
        page.delete()
        return redirect('index')
    return render(request, 'confirmar_eliminar.html', {'page': page})