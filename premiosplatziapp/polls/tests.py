#python
import datetime
#Django
from django.urls.base import reverse 
from django.test import TestCase
from django.utils import timezone
#models
from .models import Question

# Create your tests her
#models
#vistas
class QuestionModelTest(TestCase):
    
    def setUp(self):
        self.question= Question(question_text="¿quien es el mejor Course director de platzi?")
    
    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns false for questions whose pub_date is in future"""
        time = timezone.now() + datetime.timedelta(days=30)
        self.question.pub_date = time
        self.assertIs(self.question.was_publish_recently(), False)
        
        
    def test_was_published_recently_with_past_questions(self):
        """was_published_recently returns false for questions whose pub_date is in past"""
        time = timezone.now() - datetime.timedelta(days=-1, minutes= -1)
        self.question.pub_date = time
        self.assertIs(self.question.was_publish_recently(), False)
        
    def test_was_published_recently_with_present_questions(self):
        """was_published_recently returns false for questions whose pub_date is in present"""
        time=timezone.now() - datetime.timedelta(hours= 23)
        self.question.pub_date= time 
        self.assertIs(self.question.was_publish_recently(), True)
        
        
        
#test views

def create_question(question_text, days):
    """Create a question with the given "question_text", and published the given number of days offset to now (negative for question published in the past, positive for questions that have yet to be published) """
    time =timezone.now() + datetime.timedelta(days= days)
    return Question.objects.create(question_text= question_text, pub_date=time)
    


class QuestionIndexViewTest(TestCase):
    
    def test_no_questions(self):
        """if no question exis, an appropiate message is displayed"""
        response =self.client.get(reverse("polls:index")) #trae una peticion htttp de la url y la guarda en la variable
        self.assertEqual(response.status_code, 200) #revisa el status code 
        self.assertContains(response, "No polls are available.") #devuelve si no tenemos preguntas
        self.assertQuerysetEqual(response.context['latest_question_list'], []) 
        
        
    def test_future_question(self) :
        """Questions with a pub_date in the future aren't display on the index page  """
        create_question("future question", days=30)
        response= self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200 )
        self.assertQuerysetEqual( response.context['latest_question_list'],[])

        
        
    def  past_no_future_question(self):
        """Questions with a pub_date in the past are displayed on the index page  """
        question=create_question("past question", days= -10)
        response= self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code,200)
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])
        

    def test_future_question_and_past_question(self):
        """even if both past and future question exist, only past questions are displayed."""
        past_question= create_question(question_text="past question", days= -30)
        future_question= create_question(question_text="future question", days= 30)
        response= self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"],
            [past_question])
        
    def test_two_past_question(self):
        """the questions index page may display multiple questions."""
        past_question1= create_question(question_text="past question 1", days= -30)
        past_question2= create_question(question_text="past question 2", days= -40)
        response =self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"],
            [past_question1, past_question2]) 
        
    def test_two_future_question(self):
        """te questions index page aren't display multiple questions. """
        future_question1= create_question(question_text="future question 1", days= 30)
        future_question2= create_question(question_text="future question 2", days= 40)
        response= self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [])