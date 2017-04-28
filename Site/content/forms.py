""" forms.py: forms used by the app

Purpose: populate the quiz page and implement the questionnaire
Author: Tom W. Hartung
Date: Spring, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:

"""

from django import forms
from .database import Questionnaire
from .models import Questions


class QuestionnaireForm(forms.Form):

    """ A few inputs and a list of questions and multiple-choice answers """

    def __init__(self,
            quiz_size_slug=Questionnaire.DEFAULT_QUIZ_SIZE_SLUG,
            *args, **kwargs):
        """
        Create a form corresponding to the specified quiz_size_slug
        It took awhile to figure out how to create a variable-length form!
        Here is the key reference:
            http://stackoverflow.com/questions/411761/variable-number-of-inputs-with-django-forms-possible
        """
        super(QuestionnaireForm, self).__init__(*args, **kwargs)
        questions = Questions()
        question_count = Questionnaire.get_question_count_for_slug(quiz_size_slug)
        self.question_count = question_count

        for question_no in range(0, question_count):
            question_no_str = str(question_no)
            question_no_2_chars = question_no_str.zfill(2)
            question_key = 'question_' + question_no_2_chars
            form_question_no_str = str(question_no + 1)
            question_text = questions.get_question_text(question_no)
            label = form_question_no_str + '. ' + question_text
            radio_widget = forms.RadioSelect(attrs={'class': 'quiz_answer'})
            choices = questions.get_choices(question_no)
            self.fields[question_key] = forms.ChoiceField(
                widget=radio_widget, label=label, choices=choices, required=False
            )

    name = forms.CharField(
        help_text='Sharing your name allows us to get to know you better.',
        max_length=50,
        required=False)
    email = forms.EmailField(
        help_text='Enter your email address to save new or retrieve existing ' +
            'answers. (This will NOT subscribe you to our newsletter.)',
        required=False)
