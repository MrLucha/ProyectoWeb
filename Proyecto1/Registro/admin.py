from django.contrib import admin
#from .models import ModelRegistro   apuntar a todo con el .models
from Registro.models import ModelRegistro

# Register your models here.
admin.site.register(ModelRegistro)
