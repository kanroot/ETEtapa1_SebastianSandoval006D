from django.forms import ModelForm

from .models import Periodista
from django import forms


class PeriodistaCreateForm(ModelForm):
    class Meta:
        model = Periodista
        fields = ['rut', 'primerNombre', 'segundoNombre', 'apellidoPaterno', 'apellidoMaterno', 'telefono', 'direccion',
                  'numeroDireccion', 'pais']
        labels = {
            'rut': 'rut',
            'primerNombre': 'Primer Nombre',
            'segundoNombre': 'Segundo Nombre',
            'apellidoPaterno': 'Primer apellido',
            'apellidoMaterno': 'Segundo apellido',
            'telefono': 'Telefono',
            'direccion': 'direccion',
            'numeroDireccion': 'Numero direccion',
            'pais': 'Pais'
        }
        widgets = {
            'primerNombre': forms.TextInput(
                attrs={
                    'class': 'validate',
                }),
            'apellidoPaterno': forms.TextInput(
                attrs={
                    'class': 'validate',
                }),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'validate',
                }),

            'email': forms.TextInput(
                attrs={
                    'type': 'email',
                    'class': 'validate',
                }
            )
        }


class PeriodistaChangeForm(ModelForm):
    class Meta:
        model = Periodista
        fields = ['rut', 'primerNombre', 'segundoNombre', 'apellidoPaterno', 'apellidoMaterno', 'telefono', 'direccion',
                  'numeroDireccion', 'pais']
        labels = {
            'rut': 'rut',
            'primerNombre': 'Primer Nombre',
            'segundoNombre': 'Segundo Nombre',
            'apellidoPaterno': 'Primer apellido',
            'apellidoMaterno': 'Segundo apellido',
            'telefono': 'Telefono',
            'direccion': 'direccion',
            'numeroDireccion': 'Numero direccion',
            'pais': 'Pais'
        }
        widgets = {
            'primerNombre': forms.TextInput(
                attrs={
                    'class': 'validate',
                }),
            'apellidoPaterno': forms.TextInput(
                attrs={
                    'class': 'validate',
                }),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'validate',
                }),

            'email': forms.TextInput(
                attrs={
                    'type': 'email',
                    'class': 'validate',
                }
            )
        }