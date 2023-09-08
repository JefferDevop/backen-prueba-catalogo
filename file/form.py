from django import forms
from .models import Datos

import pandas as pd
from django.shortcuts import render, redirect

class CustomPersonaAdminForm(forms.ModelForm):
    class Meta:
        model = Datos
        fields = '__all__'

    def save(self, commit=True):
        # Llama al método save del modelo base (Persona) para guardar "nombre" y "correo"
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
                return redirect('exito')  # Redirige a una página de éxito
            except Exception as e:
                error_message = f"Error al procesar el archivo de Excel: {str(e)}"
            if commit:
                persona.save()
        
        return persona