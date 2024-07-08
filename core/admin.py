from django.contrib import admin
from .models import Planta, Registro, Trabajador, Combustible

# Register your models here.

admin.site.register(Planta)
admin.site.register(Registro)
admin.site.register(Trabajador)
admin.site.register(Combustible)