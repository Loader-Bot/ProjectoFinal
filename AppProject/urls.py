from django.urls import path
from django.contrib.auth.views import LogoutView

from AppProject.views import * 

urlpatterns = [
    path('registrar_usuario/', registrar, name='registrar_usuario'),
    path('login/', iniciar_sesion, name='login'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editar_usuario/', editar_usuario, name="editar_usuario"),
    path('about/', about, name='about'),
    path('avatar', avatar, name='avatar'),
    path('publicar_post/', publicar_post, name= 'publicar_post'),
    path('posts_lists/', posts_list, name = 'posts_list'),
    path('post_detalles/<int:pk>/', post_detalles, name = 'post_detalles'),
    path('editar_post/<int:pk>/', editar_post, name = 'editar_post'),
    path('borrar_post/<int:pk>/', borrar_post, name = 'borrar_post'),
    path('', index, name='index'),
    
]


