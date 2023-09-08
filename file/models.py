from django.db import models


# Modelo para los datos que se extraen del archivo Excel
class Datos(models.Model):
    campo1 = models.CharField(max_length=255)
    campo2 = models.CharField(max_length=255)
    # Puedes agregar más campos según tus necesidades

    def __str__(self):
        return str(self.id)
