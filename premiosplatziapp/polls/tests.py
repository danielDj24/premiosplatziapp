#python
import datetime
#Django
from django.urls.base import reverse 
from django.test import TestCase
from django.utils import timezone
#models
from .models import Question, Choice

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
<<<<<<< HEAD

def create_choice(pk, choice_text, votes = 0):
    """create a choice for the question with id question"""
    question = Question.objects.get(pk=pk)
    return Choice.objects.create(choice_text = choice_text, votes = votes)



=======
    
>>>>>>> e72fec9562acb703070ca6f16d2a48a57c056643


class QuestionIndexViewTest(TestCase):
    
    def test_no_questions(self):
<<<<<<< HEAD
        """if no question exist, an appropiate message is displayed"""
=======
        """if no question exis, an appropiate message is displayed"""
>>>>>>> e72fec9562acb703070ca6f16d2a48a57c056643
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
<<<<<<< HEAD
        create_question(question_text="past question", days= -30)
        create_question(question_text="future question", days= 30)
        response= self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
        
    def test_two_past_question(self):
        """the questions index page may display multiple questions."""
        create_question(question_text="past question 1", days= -30)
        create_question(question_text="past question 2", days= -40)
        response =self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], []   ) 
=======
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
>>>>>>> e72fec9562acb703070ca6f16d2a48a57c056643
        
    def test_two_future_question(self):
        """te questions index page aren't display multiple questions. """
        future_question1= create_question(question_text="future question 1", days= 30)
        future_question2= create_question(question_text="future question 2", days= 40)
        response= self.client.get(reverse("polls:index"))
<<<<<<< HEAD
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
        
    def question_without_a_choices(self):
        """question haven't a choice no display in the index view """
        question = create_question(question_text= "question ", days= -10 )
        url= reverse("polls:index")
        response = self.client.get(url)
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
        
    def question_with_a_choice(self):
        """question have a choice display in the index view"""
        question= create_question(question_text= "question text", days=-10)
        choice = create_choice(choice_text="choice text",pk=question.id )
        url= reverse("polls:index")
        response= self.client.get(url)
        self.assertQuerysetEqual(response.context["latest_question_list"], [question, choice ])
        
    
#results
        
    
class QuestionDetailView(TestCase):
    
    def test_future_question(self):
        """the detail view of a question with a pub_date in the future returns a 404 error not found"""
        future_question = create_question(question_text="future question", days=30)
        url = reverse("polls:detail", args= (future_question.id,))
        response= self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_past_question(self):
        """the detail view of a question with a pub_date in the past display the question_text"""
        past_question = create_question(question_text= "past question", days= -30)
        url= reverse("polls:detail", args=(past_question.id,))
        response= self.client.get(url)
        self.assertContains(response,past_question.question_text)
        


class ResultsViewTest(TestCase):
    
    def test_with_past_question(self):
        """the results view of a question with a pub_date in the past display the choice_text """
        past_question = create_question(question_text= "past question", days= -30)
        url= reverse("polls:results", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
        
    def test_with_future_question(self):
        """the results view of a question with a pub_date in the future returns error 404 not found """
        future_question = create_question(question_text= "future question", days= 30)
        url= reverse("polls:results", args=(future_question.id,))
        response= self.client.get(url)
        self.assertEqual(response.status_code, 404)
=======
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
>>>>>>> e72fec9562acb703070ca6f16d2a48a57c056643
