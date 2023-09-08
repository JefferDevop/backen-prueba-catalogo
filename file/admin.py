from django.contrib import admin
from .models import Datos

@admin.register(Datos)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('campo1', 'campo2')