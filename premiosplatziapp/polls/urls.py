from django.urls import path 


from . import views #el punto simboliza que vamos a importar desde el mismo paquete

app_name = "polls" #variable para referenciar los archivos 


urlpatterns = [
    #ex: /polls/ accede al index de la web
    path("", views.IndexView.as_view(), name= "index"), #ejecuta la principal con el nombre index 
    #ex: /polls/8/ accede a los detalles de la web
    path("<int:pk>/detail/Choice", views.DetailView.as_view(), name= "detail"),
    #ex: /polls/8/results/ accede a los resultados de la web
    path("<int:pk>/results/", views.ResultsView.as_view(), name= "results"),#as_view metodo que hace que se muestre la vista
    #ex: /polls/8/vote/ accede a los votos
    path("<int:pk>/vote/",views.vote, name= "vote")
]