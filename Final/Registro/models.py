from django.db import models
from Materia.models import Materia



# Create your models here.
class Ciudad(models.Model):
    nombre=models.CharField(max_length=254,null=False);

    def __str__ (self):
        return self.nombre

class Estado(models.Model):
    nombre=models.CharField(max_length=254,null=False);

    def __str__ (self):
        return self.nombre

class Genero(models.Model):
    genero=models.CharField(max_length=254,null=False);

    def __str__ (self):
        return self.genero

class EstadoCivil (models.Model):
    estadoCivil=models.CharField(max_length=254,null=False);

    def __str__ (self):
        return self.estadoCivil

class Registro(models.Model):
    nombre=models.CharField(max_length=254,null=False);
    apellidoPaterno=models.CharField(max_length=254,null=False);
    apellidoMaterno=models.CharField(max_length=254,null=False);
    Ciudad=models.ForeignKey(Ciudad,on_delete=models.CASCADE);
    #ciudad=models.CharField(max_length=254,null=True);
    Estado=models.ForeignKey(Estado,on_delete=models.CASCADE);
    #estado=models.CharField(max_length=254,null=True);
    Genero=models.ForeignKey(Genero,on_delete=models.CASCADE);
    #genero=models.CharField(max_length=254,null=True);
    EstadoCivil=models.ForeignKey(EstadoCivil,on_delete=models.CASCADE);
    #estadoCivil=models.CharField(max_length=254,null=True);
    Materia=models.ForeignKey(Materia,on_delete=models.CASCADE,null=True);

    def __str__ (self):
        return self.nombre+" "+self.apellidoPaterno+" "+self.apellidoMaterno

