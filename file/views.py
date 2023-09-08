from django.shortcuts import render
from django.contrib import admin
from .models import Datos
import pandas as pd

class DatosAdmin(admin.ModelAdmin):
    list_display = ('id', 'campo1', 'campo2')  # Mostrar campos en la vista de administración

    def save_model(self, request, obj, form, change):
        # Llama al método save_model del padre para guardar el objeto Datos
        super().save_model(request, obj, form, change)

        try:
            # Procesa el archivo y agrega los datos a la base de datos Datos
            if obj.archivo.name.endswith('.xls') or obj.archivo.name.endswith('.xlsx'):
                df = pd.read_excel(obj.archivo.path)
                for _, row in df.iterrows():
                    # Verifica si ya existe un registro con el mismo ID
                    id_existente = Datos.objects.filter(id=row['id']).first()
                    if id_existente:
                        # Actualiza el registro existente en lugar de crear uno nuevo
                        id_existente.campo1 = row['nombre_de_columna1']
                        id_existente.campo2 = row['nombre_de_columna2']
                        # Actualiza otros campos según sea necesario
                        id_existente.save()
                    else:
                        # Si no existe un registro con el mismo ID, crea uno nuevo
                        Datos.objects.create(
                            id=row['id'],
                            campo1=row['nombre_de_columna1'],
                            campo2=row['nombre_de_columna2'],
                            # Agrega más campos según tu modelo de datos
                        )
            else:
                raise Exception("El formato de archivo no es compatible.")
        except Exception as e:
            # Maneja la excepción y toma medidas apropiadas, como registrarla o mostrar un mensaje de error
            print(f"Error al procesar el archivo: {e}")
            # Puedes personalizar cómo manejar la excepción aquí

# No es necesario registrar el modelo Archivo si no quieres guardar los archivos en la base de datos
# admin.site.register(Archivo, ArchivoAdmin)

# Registra el modelo Datos con el administrador personalizado
admin.site.register(Datos, DatosAdmin)