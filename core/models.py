from django.db import models
from django.contrib.auth.models import AbstractUser

Opciones = [
    (0, 'Admin'),
    (1, 'Colaborador'),
    (2, 'Editor')
]


class User(AbstractUser):
    ##para la creacion del superuser
    bio = models.TextField(max_length=500, blank=True)


class Noticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.TextField(max_length=100, null=False, default='JUAN')
    Cuerpo = models.TextField(max_length=2000, null=False, default='JUAN')
    imagen = models.ImageField(null=True)


class Periodista(models.Model):
    categoria_usuario = models.IntegerField(default=Opciones[0][0], choices=Opciones)
    rut = models.CharField(verbose_name='Rut del colaborador', max_length=10, primary_key=True)
    imagen = models.ImageField(null=True, blank=True)
    primerNombre = models.CharField(max_length=50, null=False, default='JUAN')
    segundoNombre = models.CharField(max_length=50, null=True, default='PEDRO')
    apellidoPaterno = models.CharField(max_length=50, null=False, default='PEREZ')
    apellidoMaterno = models.CharField(max_length=50, null=True, default='GOMEZ')
    telefono = models.IntegerField(null=False, default=9999999)
    direccion = models.CharField(max_length=150, null=False, default='Direccion #1')
    numeroDireccion = models.IntegerField(null=False, default=999)
    pais = models.CharField(max_length=50, null=False, default='Chile')
