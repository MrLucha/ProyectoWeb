from django.db import models

# Create your models here.
class Materia(models.Model):
    nombre=models.CharField(max_length=254,null=False);


    def __str__ (self):
        return self.nombre