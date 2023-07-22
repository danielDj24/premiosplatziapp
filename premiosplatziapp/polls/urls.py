from django.urls import path 

from . import views #el punto simboliza que vamos a importar desde el mismo paquete


urlpatterns = [
    #ex: /polls/ accede al index de la web
    path("", views.index, name= "index"), #ejecuta la principal con el nombre index 
    #ex: /polls/8/ accede a los detalles de la web
    path("<int:question_id>/", views.detail, name= "index"),
    #ex: /polls/8/results/ accede a los resultados de la web
    path("<int:question_id>/results/", views.results, name= "index"),
    #ex: /polls/8/vote/ accede a los votos
    path("<int:question_id>/vote/",views.vote, name= "index")
]