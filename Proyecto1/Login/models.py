from django.db import models

# Create your models here.
class Profile(models.Model):
    nombre=models.CharField(max_length=254,null=False);
    apellidoPaterno=models.CharField(max_length=254,null=False);
    apellidoMaterno=models.CharField(max_length=254,null=False);
    edad=models.IntegerField(null=False);