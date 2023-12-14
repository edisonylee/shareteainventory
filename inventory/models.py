from django.db import models

# Create your models here.
class BobaProduct(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name