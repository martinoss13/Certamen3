from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Planta(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.codigo
    

class Trabajador(models.Model):
    Turno = (
        ('AM','MAÑANA'),
        ('PM','TARDE'),
        ('MM','NOCHE')
        )
    turno = models.CharField(max_length=2, choices=Turno)
    nombre = models.CharField(max_length=100)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombre
    
    
class Registro(models.Model):
    Combustible = (
        ('G93','GASOLINA93'),
        ('G95','GASOLINA95'),
        ('G97','GASOLINA97'),
        ('DIE','DIESEL_C',),
        ('DIP','DIESEL_AR'),
        ('JA1','JET'),
        ('AVG','AVGAS')
        )

    codigo_combustible = models.CharField(max_length=3, choices = Combustible)
    litros = models.FloatField()
    hora_registro = models.DateTimeField(default=timezone.now)
    fecha = models.DateTimeField(default=timezone.now)
    trabajador = models.ForeignKey(User, on_delete=models.CASCADE)

    
