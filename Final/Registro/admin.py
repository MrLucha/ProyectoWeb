from django.contrib import admin
from Registro.models import Registro
from Registro.models import Ciudad
from Registro.models import Estado
from Registro.models import Genero
from Registro.models import EstadoCivil
from Materia.models import Materia

# Register your models here.
admin.site.register(Registro)
admin.site.register(Materia)
admin.site.register(Ciudad)
admin.site.register(Estado)
admin.site.register(Genero)
admin.site.register(EstadoCivil)
