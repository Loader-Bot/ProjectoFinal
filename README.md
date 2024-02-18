# Projecto Final

CoderHouse Python Projecto Final 

# Autor:
Elaborado en su totalidad por German Gonzalez

# Requisitos
pip install Pillow


Web App con Python en Django
El Front-End utiliza Bootstrap, aplicando herencias.
Tiene dos CRUDS, usuarios y publicaciones.
La NavBar contiene los accesos a las siguientes secciones:
-Home
-Acerca de
-Publicar (demanda que el usuario haya iniciado sesion previamente)
-Login/Logout
-Registar Usuario
-Editar Perfil
-Editar Imagen de Perfil

# Video
https://drive.google.com/file/d/17jbwGNn-71kquKHR9ILck5HXL4sp1E94/view?usp=sharing

# Pagina Principal

Contiene la NavBar con todas las opciones y se pueden ver todos los posts publicados.
Enlace: http://127.0.0.1:8000/app/

# Pagina Login
Donde el usuario ya registrado puede iniciar sesion. De ser exitoso devuelve al sitio HOME.

Enlace: http://127.0.0.1:8000/app/login

# Pagina de registro de usuario
Donde puede crearse un nuevo usuario.

Enlace: http://127.0.0.1:8000/app/registrar_usuario

# Pagina para editar usuario:

Enlace: http://127.0.0.1:8000/app/editar_usuario

# Pagina para publicar noticias:

Se puede poner un titulo, descripcion , cuerpo e imagen. Se guarda la autoria, fecha de entrega, y solo el usuario que creo una publicacion puede editarla o borrarla.

Enlace: http://127.0.0.1:8000/app/publicar_post

# Detalle de Pagina

Permite acceder a cada articulo en su totalidad

Enlace: http://127.0.0.1:8000/app/post_detalles/1

# Pagina para editar publicaciones:

Enlace: http://127.0.0.1:8000/app/login/editar_post/1

# Pagina para borrar publicacones:
Requiere confirmacion y que el usuario correspondiente haya iniciado sesion para que se pueda hacer:

Enlace: http://127.0.0.1:8000/app/borrar_post/1
