from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse #permite ejecutar una respuesta http

from .models import Question #importamos el modelo Question 

def index(request):
    latest_question_list = Question.objects.all()
    '''index = trae todas las preguntas 
    
    
        return render= le damos las variables que puede usarse en el html con formato diccionario, y para mostrarlo en la web 
    '''
    context= {"latest_question_list" : latest_question_list}
    
    return render(request,"polls/index.html",context) 


def detail(request, question_id) : 
    """details = nos muestra los detalles de la pregunta que escojamos, segun su llaves
        question = obtiene las preguntas o suelta un error 404 segun su pk
        context = diccionario donde obtenemos las clave llave valor que nos devuelve la funcion
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {"question" :question}
    return render(request,"polls/detail.html",context)


    
def results(request,question_id ): #func que nos devuelve las respuestas de la pregunta con el id 
    return HttpResponse(f"estas viendo los resultados de la pregunta numero {question_id}")


def vote(request,question_id): #func que nos devuelve a quien le votamos 
    return HttpResponse(f"estas votando a la pregunta numero {question_id}")