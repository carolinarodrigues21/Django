from django.test import TestCase

import datetime 

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):

    #tests are recognized as those whose name begins with test

    #The test informs us which test failed and even the line on which the failure occurred.
    def test_was_published_recently_with_future_question(self):

        """
        was_published_recently() returns False for questions whose
        pub_date is in the future

        """

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)                       #creates a Question instance whose pub_date field is 30 days in the future
        self.assertIs(future_question.was_published_recently(), False)

