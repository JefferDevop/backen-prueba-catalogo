from django import forms
from .models import Datos
from django.contrib import messages
import pandas as pd
from django.shortcuts import render, redirect

class CustomPersonaAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Datos
        fields = '__all__'

    def save(self, commit=True):
        # Accede al objeto request utilizando self.request
        if self.request:
            # Llama al método save del modelo base (Datos) para guardar los campos del modelo
            persona = super().save(commit=False)

            # Ahora, procesa el archivo y guarda la información
            uploaded_file = self.cleaned_data.get('file')
            if uploaded_file:
                try:
                    df = pd.read_excel(uploaded_file)
                    for _, row in df.iterrows():
                        persona = Datos(
                            campo1=row['Nombre'],
                            campo2=row['Correo'],
                            # Agrega otros campos y asigna los valores desde el archivo
                        )
                        persona.save()
                    messages.success(self.request, "¡Archivo de Excel procesado y datos guardados con éxito!")
                    return redirect('exito')  # Redirige a una página de éxito
                except Exception as e:
                    error_message = f"Error al procesar el archivo de Excel: {str(e)}"
            else:
                error_message = "Formulario no válido. Asegúrate de seleccionar un archivo."