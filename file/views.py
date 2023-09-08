import pandas as pd
from django.shortcuts import render, redirect
from .form import FileUploadForm
from .models import Datos

def subir_excel(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            archivo_excel = request.FILES['archivo']
            try:
                df = pd.read_excel(archivo_excel)
                for _, row in df.iterrows():
                    persona = Datos(
                        campo1=row['Nombre'],
                        campo2=row['Correo electrónico'],
                    )
                    persona.save()
                return redirect('exito')  # Redirige a una página de éxito
            except Exception as e:
                error_message = f"Error al procesar el archivo de Excel: {str(e)}"
        else:
            error_message = "Formulario no válido. Asegúrate de seleccionar un archivo."
    else:
        form = FileUploadForm()
        error_message = None

    return render(request, 'subir_excel.html', {'form': form, 'error_message': error_message})