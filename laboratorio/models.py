from django.db import models
from datetime import datetime

# Create your models here.
class Laboratorio(models.Model):
    nombre = models.CharField(max_length = 128)
    ciudad = models.CharField(max_length = 128, default = "")
    pais = models.CharField(max_length = 128, default = "")

    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length = 128)
    especialidad = models.CharField(max_length = 128, default = "")
    laboratorio = models.OneToOneField(Laboratorio, on_delete = models.PROTECT)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length = 128)
    laboratorio = models.ForeignKey(Laboratorio, on_delete = models.PROTECT)
    f_fabricacion = models.DateField() # (validators=[MinValueValidator(datetime.date(2015,01,01))])
    p_costo = models.DecimalField(max_digits = 12, decimal_places = 2)
    p_venta = models.DecimalField(max_digits = 12, decimal_places = 2)

    def __str__(self):
        return self.nombre