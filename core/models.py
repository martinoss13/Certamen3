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
        ('MAÑANA','AM'),
        ('TARDE','PM'),
        ('NOCHE','MM')
        )
    turno = models.CharField(max_length=10, choices=Turno)
    nombre = models.CharField(max_length=100)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombre
    
    
class Registro(models.Model):
    Combustible = (
        ('GASOLINA93','G93'),
        ('GASOLINA95','G95'),
        ('GASOLINA97','G97'),
        ('DIESEL_C', 'DIE'),
        ('DIESEL_AR','DIP'),
        ('JET','JA1'),
        ('AVGAS','AVG')
        )

    codigo_combustible = models.CharField(max_length=10, choices = Combustible)
    litros = models.FloatField()
    hora_registro = models.DateTimeField()
    fecha = models.DateTimeField(default=timezone.now)
    trabajador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre
    
