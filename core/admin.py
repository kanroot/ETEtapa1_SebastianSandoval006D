from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import *

admin.site.register(Periodista)
admin.site.register(Noticia)
admin.site.unregister(Group)
