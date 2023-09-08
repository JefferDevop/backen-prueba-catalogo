from django.shortcuts import render, redirect
from .form import CustomPersonaAdminForm

def subir_excel(request):
    if request.method == 'POST':
        form = CustomPersonaAdminForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            form.save()
            return redirect('exito')  # Redirige a una página de éxito
    else:
        form = CustomPersonaAdminForm(request=request)  # Asegúrate de pasar 'request'
    return render(request, 'subir_excel.html', {'form': form})

