from django.urls import path
from django.contrib.auth.views import LogoutView

from AppProject.views import * 

urlpatterns = [
    path('registrar_usuario/', registrar, name='registrar_usuario'),
    path('login/', iniciar_sesion, name='login'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('', index, name='index'),
]