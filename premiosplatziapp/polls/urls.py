from django.urls import path

from . import views #el punto simboliza que vamos a importar desde el mismo paquete 


urlpatterns = [
    path("", views.index, name= "index")
]