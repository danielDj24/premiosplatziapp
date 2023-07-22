from django.contrib import admin
from .models import Question, Choice #importamos los modelos que estan dentro de esta carpeta

admin.site.register([Question, Choice]) #con esta linea le decimos al proyecto que vamos a utilizar el modelo desde la web 