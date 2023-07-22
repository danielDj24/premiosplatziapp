import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model): #modelo para las preguntas 
    #el framewrok crea un id escalonable
    question_text = models.CharField(max_length=200) 
    pub_date = models.DateTimeField("date published")
    
    def __str__(self) : #todo metodo dentro de una clase lleva como parametro self
        return self.question_text # cada vez  que invoquemos una pregunta, en la consola o codigo, nos suelte el valor
    
    
    def was_publish_recently(self): #meotodo que retorna true o f si la public se hizo recientemente
        return self.pub_date >= timezone.now() - datetime.timedelta(days= 1) #restamos al tiempo actual un dia 
        
    
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length= 200) #respuestas que retornaremos 
    votes = models.IntegerField(default= 0) #campo de numeros enteros que incrementa desde cero mientras hacemos la app
    
    def __str__(self): # metodo para que nos devuelva el texto 
        return self.choice_text