from django.shortcuts import render
from django.http import HttpResponse #permite ejecutar una respuesta http

def index(request):
    return HttpResponse('Hello world')