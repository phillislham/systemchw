from django.http import HttpResponse
from django.shortcuts import render

from employees.models import Registro


# #Create your views hare.
def bienvenido(request):
     registro_var = Registro.objects.count()
     registros = Registro.objects.all()
     return render(request, 'bienvenido.html', {'registro':registro_var, 'registros': registros})