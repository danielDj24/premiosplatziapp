from django.db import models

class Question(models.Model): 
    #el framewrok crea un id escalonable
    question_text = models.CharField(max_length=200) 
    pub_date = models.DateTimeField("date published")
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length= 200) #respuestas que retornaremos 
    votes = models.IntegerField(default= 0) #campo de numeros enteros que incrementa desde cero mientras hacemos la app