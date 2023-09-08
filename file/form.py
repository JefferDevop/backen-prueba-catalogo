from django import forms

class FileUploadForm(forms.Form):
    archivo = forms.FileField()