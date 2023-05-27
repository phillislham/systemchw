from django.shortcuts import render

from employees.models import Registro


# Create your views here.
def detalle_registro(request, id):
    registro = Registro.objects.get(pk=id)
    return render(request, 'empleados/detail.html', {'registro': registro})