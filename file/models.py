from django.db import models


# Modelo para los datos que se extraen del archivo Excel
class Datos(models.Model):
    campo1 = models.CharField(max_length=255, null=True, blank=True)
    campo2 = models.CharField(max_length=255, null=True, blank=True)
    archivo_excel = models.FileField(upload_to='archivos_excel/', null=True, blank=True)

    def __str__(self):
        return self.campo1

