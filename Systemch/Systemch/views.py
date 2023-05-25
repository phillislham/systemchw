from django.shortcuts import render

from appweb.models import Registro


#Create your views hare.
def detalleRegistro(request, id):
    registro = Registro.objects.get(pk=id)
    return render(request, 'registro/vistas.html', {'registro': registro})
