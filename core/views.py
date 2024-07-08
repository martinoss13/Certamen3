from django.shortcuts import render, redirect
from .models import Registro, Trabajador, Combustible
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404






# Create your views here.
def index(request):
    permiso = request.user.groups.all()
    registros = Registro.objects.all()
    usuario = request.user


    data={
        'permiso': permiso,
        'registros': registros,
        'usuario': usuario,
    }
    
    if usuario.groups.filter(name='Operador').exists():
        data['es_operador'] = True


    return render(request, "core/index.html", data)

@login_required
def registro(request, registro_id=None):
    error_message = None
    registro_instance = None

    if registro_id:
        registro_instance = get_object_or_404(Registro, id=registro_id)

    if request.method == 'POST':
        codigo_combustible = request.POST.get('codigo_combustible')
    
        print(codigo_combustible)
        combustible = get_object_or_404(Combustible, codigo = codigo_combustible)
        
        litros = request.POST.get('litros')
        
        if codigo_combustible and litros:
            try:
                litros = float(litros)
                if registro_instance:
                    registro_instance.codigo_combustible = combustible
                    registro_instance.litros = litros
                    registro_instance.hora_registro = timezone.now()
                    registro_instance.save()
                else:
                    Registro.objects.create(
                        codigo_combustible=combustible,
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

    trabajador = Trabajador.objects.get(user=request.user)
    combustibles = Combustible.objects.filter(planta=trabajador.planta)

    contexto = {
        'error_message': error_message,
        'registro': registro_instance if registro_instance else Registro(),
        'combustibles': combustibles,
    }
    return render(request, 'core/formulario.html', contexto)



    