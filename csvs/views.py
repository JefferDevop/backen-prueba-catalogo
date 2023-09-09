from django.shortcuts import render
from django.http import HttpResponse

def upload_file_view(request):
    return HttpResponse('File')
