from django.shortcuts import render
from django.http import HttpResponse #permite ejecutar una respuesta http


def index(request):
    return HttpResponse('Estas en la pagina principal de premios platzi app')


def detail(request, question_id) : #nos muestra los detalles de la pregunta que escojamos, segun su llaves
    return HttpResponse(f"estas viendo la pregunta numero {question_id}")


def results(request,question_id ): #func que nos devuelve las respuestas de la pregunta con el id 
    return HttpResponse(f"estas viendo los resultados de la pregunta numero {question_id}")


def vote(request,question_id): #func que nos devuelve a quien le votamos 
    return HttpResponse(f"estas votando a la pregunta numero {question_id}")