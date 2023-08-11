from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect #permite ejecutar una respuesta http
from django.urls import reverse #importamos la funcion reverse
from django.views import generic 
from django.utils import timezone

from .models import Question, Choice #importamos el modelo Question 

'''
def index(request):
    latest_question_list = Question.objects.all()
    index = trae todas las preguntas 
    
    
        return render= le damos las variables que puede usarse en el html con formato diccionario, y para mostrarlo en la web 
    ---------------------------------------------------------
    context= {"latest_question_list" : latest_question_list}
    
    return render(request,"polls/index.html",context) 
'''
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]  #trae las preguntas del momento actual hasta el pasado

'''
def detail(request, question_id) : 
    """details = nos muestra los detalles de la pregunta que escojamos, segun su llaves
        question = obtiene las preguntas o suelta un error 404 segun su pk
        context = diccionario donde obtenemos las clave llave valor que nos devuelve la funcion
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {"question" :question}
    return render(request,"polls/detail.html",context)
'''

class DetailView(generic.DetailView): 
    model = Question
    template_name = "polls/detail.html"#nobre del archivo html
    
    
    

'''    
def results(request,question_id ): #se ejecuta despues de vote
    question= get_object_or_404(Question, pk=question_id)
    return render(request,"polls/result.html", {
        "question" : question
    }  )
'''    
class ResultsView(generic.DetailView): 
    model = Question
    template_name = "polls/results.html" #nobre del archivo html    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            "question": question,
            "error_message": "¡No elegiste una respuesta! "
        })
    else:  # * Si todo salió bien entonces haz este bloque
        selected_choice.votes += 1
        selected_choice.save()
        # ! Es buena práctica hacer redirect después de que el usuario usó un formulario
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))