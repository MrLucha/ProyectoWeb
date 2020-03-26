from django.db import models

# Create your models here.
class Materia(models.Model):
    nombre=models.CharField(max_length=254,null=False);

class Alumno(models.Model):
    nombre=models.CharField(max_length=254,null=False);
    carrera=models.CharField(max_length=254,null=True);
    edad=models.IntegerField(null=True);
    direccion=models.CharField(max_length=254,null=True);
    genero=models.CharField(max_length=254,null=True);
    matricula=models.IntegerField(null=False);
    Materia=models.ForeignKey(Materia,on_delete=models.CASCADE);
