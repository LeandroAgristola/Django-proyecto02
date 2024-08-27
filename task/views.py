from django.shortcuts import render
from django.http import HttpResponse #importamos el paquete de respuesta http

# Create your views here.

def helloword(request):
    return HttpResponse('hola mundo')
