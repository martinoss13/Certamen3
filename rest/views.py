from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RegistroSerializer
from core.models import Registro

# Create your views here.

class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer