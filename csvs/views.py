from django.shortcuts import render
from .forms import CsvModelForm
# from django.http import HttpResponse

def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
    return render(request, 'csvs/upload.html', {'form': form})
