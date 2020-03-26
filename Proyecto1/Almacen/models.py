from django.db import models

# Create your models here.
class Almacen(models.Model):
    caracteristicas=models.CharField(max_length=254,null=False);
    nombreProducto=models.CharField(max_length=254,null=False);
    fechaCaducidad=models.CharField(max_length=254,null=False);
    fechaProducto=models.CharField(max_length=254,null=False);
    cantidadProducto=models.IntegerField(null=False);
    ventasPorPieza=models.CharField(max_length=254,null=False);
    
