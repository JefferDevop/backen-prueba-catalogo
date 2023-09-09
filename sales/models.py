from django.db import models

# Create your models here.
class Sale(models.Model):
    product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    total = models.FloatField(blank=True, default=0)
    updated = models.DateField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product}-{self.quantity}"