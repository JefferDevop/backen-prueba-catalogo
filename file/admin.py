from django.contrib import admin
from django.urls import path
from . import views

@admin.site.admin_view
def cargar_archivo(request):
    
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo']

            # Procesa el archivo y guarda los datos en el modelo Datos
            if archivo.name.endswith('.xls') or archivo.name.endswith('.xlsx'):
                df = pd.read_excel(archivo)
                for _, row in df.iterrows():
                    id_existente = Datos.objects.filter(id=row['id']).first()
                    if id_existente:
                        id_existente.campo1 = row['nombre_de_columna1']
                        id_existente.campo2 = row['nombre_de_columna2']
                        # Actualiza otros campos según sea necesario
                        id_existente.save()
                    else:
                        Datos.objects.create(
                            id=row['id'],
                            campo1=row['nombre_de_columna1'],
                            campo2=row['nombre_de_columna2'],
                            # Agrega más campos según tu modelo de datos
                        )
                # Redirige a una página de éxito o muestra un mensaje de éxito
                return redirect('exito')  # Cambia 'exito' por la URL de tu página de éxito
            else:
                # Muestra un mensaje de error si el formato de archivo no es compatible
                form.add_error('archivo', 'El formato de archivo no es compatible.')
        else:
            form = FileUploadForm()
        return render(request, 'admin/cargar_archivo.html', {'form': form})
            # Recuerda importar y utilizar pandas como se muestra en tu código original
            # Luego redirige o muestra un mensaje de éxito
    else:
        form = FileUploadForm()
    return render(request, 'admin/cargar_archivo.html', {'form': form})

admin.site.add_action(cargar_archivo)
