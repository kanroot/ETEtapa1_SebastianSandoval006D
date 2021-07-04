
from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index.html'),
    path('noticias/', mostrar_noticias, name='noticias.html'),
    path('contacto/', contacto, name='contacto.html'),
    path('quienessomos/', quienessomos, name='quienessomos.html'),
    path('ver/usuarios', crud_ver_usuario, name='ver_usuarios.html'),
    path('crear/usuarios', crud_crear_usuario, name='crear_usuario.html'),
    path('modificar/<rut>', crud_modificar_usuario, name='modificar_usuario.html'),
    path('eliminado/<rut>', crud_eliminar_usuario, name='eliminar_usuario')
]