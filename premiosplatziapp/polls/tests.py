#python
import datetime
#Django
from django.test import TestCase
from django.utils import timezone
#models
from .models import Question

# Create your tests her
#models
#vistas
class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns false for questions whose pub_date is in future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿quien es el mejor Course director de platzi?" ,pub_date=time)
        self.assertIs(future_question.was_publish_recently(), False)