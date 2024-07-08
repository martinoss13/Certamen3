from rest_framework import serializers
from core.models import Registro, Combustible

class CombustibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combustible
        fields = ('codigo',)

class RegistroSerializer(serializers.ModelSerializer):
    codigo_combustible = CombustibleSerializer()
    class Meta:
        model = Registro
        exclude = ['hora_registro','fecha','trabajador', 'id']
