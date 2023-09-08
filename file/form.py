from django import forms
from .models import Datos

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
            # Procesa el archivo aquí, por ejemplo, utilizando pandas
            # Luego, asigna los valores procesados a los campos del modelo
            # persona.nombre = ...
            # persona.correo = ...
            # ...
            if commit:
                persona.save()
        
        return persona