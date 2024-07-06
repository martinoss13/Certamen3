from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Registro
from django.utils import timezone
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    permiso = request.user.groups.all()
    registros = Registro.objects.all()
    data={
        'permiso': permiso,
        'registros': registros,
    }
    return render(request, "core/index.html", data)

@login_required
def registro(request):
    if request.method == 'POST':
        codigo_combustible = request.POST.get('codigo_combustible')
        litros = request.POST.get('litros')
        
        if codigo_combustible and litros:
            try:
                litros = float(litros)
                Registro.objects.create(
                    codigo_combustible=codigo_combustible,
                    litros=litros,
                    trabajador=request.user,
                    hora_registro=timezone.now(),
                    fecha=timezone.now()
                )
                return redirect('/')  
            except ValueError:
                error_message = "El valor de litros debe ser numérico."
        else:
            error_message = "Todos los campos son requeridos."
        
        contexto = {
            'error_message': error_message,
            'registro': Registro
        }
        return render(request, 'core/formulario.html', contexto)
    
    return render(request, 'core/formulario.html', {'registro': Registro()})