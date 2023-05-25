from django.http import HttpResponse
from django.shortcuts import render

from appweb.models import Registro


# Create your views here.
def bienvenido(request):
    numero_registros = Registro.objects.count()
    registros = Registro.objects.all()
    return render(request, 'bienvenido.html', {'Numero de registros': numero_registros, 'registros': registros})