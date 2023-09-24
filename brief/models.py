from django.db import models
from push_notifications.models import GCMDevice



class Brief(models.Model):
    usuario = models.CharField(
        max_length=50, verbose_name=(u'Usuario anonimo'), blank='True', null='True', default='Anonimo')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Usuario Anonimo'
        verbose_name_plural = 'Usuarios Anonimos'

    def __str__(self):
        return self.company
    
class BriefHistorical(models.Model):
    usuario = models.ForeignKey(
        Brief, on_delete=models.CASCADE, verbose_name=("Usuario")
    )
    start_datetime = models.DateTimeField(auto_now_add=True, verbose_name=("Ingresó"))
    end_datetime = models.DateTimeField(auto_now=True, verbose_name=("Salió"))
    total_hours = models.FloatField(null=True, blank=True, verbose_name=("En-Linea"))

    def save(self, *args, **kwargs):
        if self.start_datetime and self.end_datetime:
            time_difference = self.end_datetime - self.start_datetime
            # La diferencia se almacena en segundos, así que la convertimos a horas
            self.total_hours = time_difference.total_seconds() / 3600
        else:
            self.total_hours = None
        super(BriefHistorical, self).save(*args, **kwargs)

    def __str__(self):
        return f"Total de horas: {self.total_hours}"
    

    class MyDevice(GCMDevice):
        brief = models.ForeignKey(Brief, on_delete=models.CASCADE)