from django.http import HttpResponse
from django.shortcuts import render

# Cretae your wiews here
def bienvenido(request):
    return HttpResponse('Hola Django des de ')