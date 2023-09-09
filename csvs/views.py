from django.shortcuts import render
from .forms import CsvModelForm
from .models import Csv
import csv
from sales.models import Sale
# from django.http import HttpResponse


def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i==0:
                    pass
                else:
                    row = "".join(row)     
                    row = row.replace(";", " ")    
                    row = row.split()            
                    product = row[1].upper()
                    
            obj.activated = True
            obj.save()
    return render(request, "csvs/upload.html", {"form": form})
