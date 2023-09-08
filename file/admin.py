from django.contrib import admin
from .models import Datos
from .form import CustomPersonaAdminForm

class PersonaAdmin(admin.ModelAdmin):
    form = CustomPersonaAdminForm

admin.site.register(Datos, PersonaAdmin)