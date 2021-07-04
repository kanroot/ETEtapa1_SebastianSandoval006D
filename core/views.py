from django.shortcuts import render, redirect

from core.models import Periodista, Noticia
from .forms2 import PeriodistaCreateForm, PeriodistaChangeForm


def index(request):
    return render(request, 'index.html')


def noticias(request):
    return render(request, 'noticias.html')


def quienessomos(request):
    return render(request, 'quienessomos.html')


def contacto(request):
    return render(request, 'contacto.html')


def crud_ver_usuario(request):
    # compruebo si esta authenticated
    if request.user.is_authenticated:
        users = Periodista.objects.all()
        data = {
            'users': users
        }
        return render(request, 'CRUD/ver_usuarios.html', data)

    return redirect('index.html')


def crud_crear_usuario(request):
    if request.user.is_authenticated:
        data = {
            'form': PeriodistaCreateForm()
        }

        if request.method == 'POST':
            formulario = PeriodistaCreateForm(request.POST)

            if formulario.is_valid:
                formulario.save()

            data = {
                'mensaje': 'Usuario escrito satisfactoriamente'
            }

        return render(request, 'CRUD/crear_usuario.html', data)
    return redirect('index.html')


def crud_modificar_usuario(request, rut):
    if request.user.is_authenticated:
        user = Periodista.objects.get(rut=rut)

        data = {
            'form': PeriodistaChangeForm(instance=user)
        }

        if request.method == 'POST':
            formulario = PeriodistaChangeForm(data=request.POST, instance=user)

            if formulario.is_valid:
                formulario.save()

            data = {
                'mensaje': f'Usuario {user.rut} fue modificado con éxito'
            }

        return render(request, 'CRUD/modificar_usuario.html', data)
    return redirect('index.html')


def crud_eliminar_usuario(request, rut):
    Periodista.objects.filter(rut=rut).delete()

    return redirect(crud_ver_usuario)


def modificar_periodista(request, rut):
    if request.user.is_authenticated:
        users = Periodista.objects.get(rut=rut)
        data = {
            'users': PeriodistaChangeForm(instance=users)
        }
        if request.method == 'POST':
            formulario = PeriodistaChangeForm(data=request.POST, instance=users)
            if formulario.is_valid:
                formulario.save()
                data['users'] = formulario
            data = {
                'mensaje': f'Usuario {users.rut} fue modificado con éxito'
            }


def mostrar_noticias(request):
    users = Noticia.objects.all()
    data = {
        'users': users
    }
    return render(request, 'noticias.html', data)
