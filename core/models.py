from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings


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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="trabajador")
    turno = models.CharField(max_length=2, choices=Turno)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.user.username
    
    
class Combustible(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre

class Registro(models.Model):
    
    codigo_combustible = models.ForeignKey(Combustible, on_delete=models.CASCADE)
    litros = models.FloatField()
    hora_registro = models.DateTimeField(default=timezone.now)
    fecha = models.DateTimeField(default=timezone.now)
    trabajador = models.ForeignKey(User, on_delete=models.CASCADE)

    
