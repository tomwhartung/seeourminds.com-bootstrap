""" Contains the database models and access routines for our app.

Purpose: contains the methods for accessing and updating data in the database
Author: Tom W. Hartung
Date: Winter, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none, yet)
"""

import os
from django.contrib import messages
from django.db import models
from django.http import QueryDict
from django.utils import timezone

DJANGO_DEBUG = os.environ.get('DJANGO_DEBUG')
RUNNING_LOCALLY = os.environ.get('RUNNING_LOCALLY')

"""
There are 88 questions, and the ones I have the most confidence in are
nearer the beginning, with the "fun," experimental ones at the end.
It is desireable that the number of questions be divisible by 4 but not 8,
so that there is an odd number of questions for each pair of opposites.
"""
TINY = 'T'             # 4 = 1 * 4 (for testing, not available in production)
XX_SMALL = '2XS'       # 12 = 3 * 4
EXTRA_SMALL = 'XS'     # 20 = 5 * 4
SMALL = 'S'            # 28 = 7 * 4
MEDIUM = 'M'           # 44 = 11 * 4
LARGE = 'L'            # 60 = 15 * 4
EXTRA_LARGE = 'XL'     # 76 = 19 * 4
XX_LARGE = '2XL'       # 88 = 22 * 4


class Questionnaire(models.Model):

    """
    Define columns and save a person's questionnaire answers in the database.
    """

    QUIZ_SIZE_CHOICES = (
        (TINY, 'Tiny'),
        (XX_SMALL, '2X Small'),
        (EXTRA_SMALL, 'Extra Small'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (EXTRA_LARGE, 'Extra Large'),
        (XX_LARGE, '2X Large'),
    )
    DEFAULT_QUIZ_SIZE = MEDIUM
    DEFAULT_QUIZ_SIZE_SLUG = 'medium'
    QUIZ_VERSION = '1.0'

    name = models.CharField(
            blank=True,
            default='',
            max_length=200)
    email = models.EmailField(
            blank=False,
            db_index=True,
            max_length=200,
            unique=True)
    size = models.CharField(
            choices=QUIZ_SIZE_CHOICES,
            default=DEFAULT_QUIZ_SIZE,
            max_length=3)
    version = models.CharField(
            default=QUIZ_VERSION,
            max_length=10)
    date_created = models.DateTimeField(
            default=timezone.now)
    date_updated = models.DateTimeField(
            default=timezone.now)

    def save_questionnaire(self, cleaned_data, quiz_size_slug=DEFAULT_QUIZ_SIZE_SLUG):
        """
        If we have an email, save the questionnaire data, along with the answers
        There is no sense saving it if we do not have an email address!
        (We also do this check in the view, so it's redundant I know.)
        Note: the validation criteria for emails used by the db is stronger
            than it is for forms...!
        """
        email = cleaned_data['email']
        if email == '':
            return False

        existing_questionnaire = self.load_questionnaire(email)

        if existing_questionnaire != None:
            self.id = existing_questionnaire.id

        name = cleaned_data['name']
        self.name = name
        self.email = email
        self.size = self.get_quiz_size_abbr_for_slug(quiz_size_slug)
        self.save()
        # print('Questionnaire.save_questionnaire - saved:', self.__str__())

        for form_field_name in sorted(cleaned_data):
            if form_field_name.startswith("question_"):
                question_int = int(form_field_name.replace("question_", ""))
                answer_str = cleaned_data[form_field_name]
                answer_int = int(answer_str)
                answer_db = Answer()
                answer_db.save_answer(self.id, question_int, answer_int)
        return self

    def add_answers(self, email, request):
        """ Load answers from db and add them to the request.POST """
        questionnaire = self.load_questionnaire(email)
        answers_dict = self.load_answers(questionnaire, request)
        #
        # If there are no answers found,
        #   return only the name email address in the request
        #
        if answers_dict == None:
            not_found_msg = 'Unable to find questionnaire for ' + email
            messages.add_message(request, messages.ERROR, not_found_msg)
            new_request_data = QueryDict('', mutable=True)
            new_data = {
                'name': request.POST['name'],
                'email': request.POST['email'],
            }
            new_request_data.update(new_data)
        else:
            new_request_data = request.POST.copy()
            if new_request_data['name'] == '':
                new_request_data['name'] = questionnaire.name
            for question_key in answers_dict:
                new_request_data[question_key] = answers_dict[question_key]

        return new_request_data

    def load_answers(self, questionnaire, request):
        """ Load and return the answers for the passed-in questionnaire """
        ans_query_set = None

        if questionnaire == None:
            answers_dict = None
        else:
            answers_dict = {}
            try:
                ans_query_set = Answer.objects.filter(questionnaire=questionnaire)
            except BaseException as exc:
                print('Questionnaire.load_answers ERROR',
                    '(questionnaire = "' + questionnaire + '"):',
                    'Questionnaire found but unable to get ans_query_set!',
                    'exc: "' + str(exc) + '"')

        if ans_query_set != None:
            for ans in ans_query_set:
                question_no_str = str(ans.question_id)
                question_no_2_chars = question_no_str.zfill(2)
                question_key = 'question_' + question_no_2_chars
                answer_str = str(ans.answer)
                # print('Questionnaire - question_key-str(answer_list):',
                #    question_key + '-' + str(answer_str))
                answers_dict[question_key] = answer_str

        return answers_dict

    def load_questionnaire(self, email):
        """ Load and return the questionnaire for the passed-in email """
        try:
            questionnaire = Questionnaire.objects.get(email__iexact=email)
        except:
            questionnaire = None
        return questionnaire

    @classmethod
    def get_quiz_size_slugs_list(cls):
        """ Returns a list of the available quiz size choices """
        quiz_size_slugs = []

        if RUNNING_LOCALLY:
            quiz_size_slugs.append('tiny')

        quiz_size_slugs.append('xx-small')
        quiz_size_slugs.append('extra-small')
        quiz_size_slugs.append('small')
        quiz_size_slugs.append('medium')
        quiz_size_slugs.append('large')
        quiz_size_slugs.append('extra-large')
        quiz_size_slugs.append('xx-large')
        return quiz_size_slugs

    @classmethod
    def get_quiz_menu_data(cls):
        """ Returns a list of the quiz size data needed to create the menu """
        quiz_menu_data = []
        quiz_size_slugs = cls.get_quiz_size_slugs_list()

        for quiz_size_slug in quiz_size_slugs:
            size_text = cls.get_quiz_size_text_for_slug(quiz_size_slug)
            quiz_menu_data.append([quiz_size_slug, size_text])

        return quiz_menu_data

    @classmethod
    def get_quiz_list_data(cls):
        quiz_size_slugs = cls.get_quiz_size_slugs_list()
        quiz_list_data = []

        for quiz_size_slug in quiz_size_slugs:
            size_text = cls.get_quiz_size_text_for_slug(quiz_size_slug)
            question_count = cls.get_question_count_for_slug(quiz_size_slug)
            quiz_size_abbr = cls.get_quiz_size_abbr_for_slug(quiz_size_slug)
            button_classes = cls.get_button_classes_for_slug(quiz_size_slug)
            data_for_slug = [
                quiz_size_slug,
                size_text,
                question_count,
                quiz_size_abbr,
                button_classes
            ]
            quiz_list_data.append(data_for_slug)

        return quiz_list_data

    @classmethod
    def get_quiz_size_abbr_for_slug(cls, quiz_size_slug):
        """ Returns the corresponding constant for passed in quiz_size_slug """
        quiz_size_constant_for_slug = {
            "tiny": TINY,
            "xx-small": XX_SMALL,
            "extra-small": EXTRA_SMALL,
            "small": SMALL,
            "medium": MEDIUM,
            "large": LARGE,
            "extra-large": EXTRA_LARGE,
            "xx-large": XX_LARGE,
        }
        return quiz_size_constant_for_slug[quiz_size_slug]

    @classmethod
    def get_question_count_for_slug(cls, quiz_size_slug):
        """ Returns the number of questions for passed in quiz_size_slug """
        question_count_for_slug = {
            "tiny": 4,
            "xx-small": 12,
            "extra-small": 20,
            "small": 28,
            "medium": 44,
            "large": 60,
            "extra-large": 76,
            "xx-large": 88,
        }
        return question_count_for_slug[quiz_size_slug]

    @classmethod
    def get_quiz_size_text_for_slug(cls, quiz_size_slug):
        """ Returns the quiz size_text for the passed in quiz_size_slug """
        quiz_size_slugs_to_text = {
            'tiny': 'Tiny',
            'xx-small': '2X Small',
            'extra-small': 'Extra Small',
            'small': 'Small',
            'medium': 'Medium',
            'large': 'Large',
            'extra-large': 'Extra Large',
            'xx-large': '2X Large',
        }
        return quiz_size_slugs_to_text[quiz_size_slug]

    @classmethod
    def get_button_classes_for_slug(cls, quiz_size_slug):
        """ Returns the quiz button_classes for the passed in quiz_size_slug """
        quiz_size_slugs_to_button_classes = {
            'tiny': 'btn btn-danger btn-xs',
            'xx-small': 'btn btn-warning btn-sm',
            'extra-small': 'btn btn-warning btn-sm',
            'small': 'btn btn-success btn-md',
            'medium': 'btn btn-success btn-md',
            'large': 'btn btn-success btn-md',
            'extra-large': 'btn btn-primary btn-lg',
            'xx-large': 'btn btn-primary btn-lg',
        }
        return quiz_size_slugs_to_button_classes[quiz_size_slug]

    def __str__(self):
        name_email_size = self.name + '/' + self.email + '/' + self.size
        return name_email_size


class Answer(models.Model):

    """ Define a table in which to save each individual answer """

    questionnaire = models.ForeignKey(
        'content.Questionnaire',
        on_delete=models.CASCADE)
    question_id = models.IntegerField(
        default=0,
        db_index=True)
    answer = models.IntegerField(
        default=0)

    def save_answer(self, questionnaire_id, question_id, answer):
        """ Save the questionnaire answers """
        existing_answer = self.load_answer(questionnaire_id, question_id)

        if existing_answer != None:
            self.id = existing_answer.id

        self.questionnaire_id = questionnaire_id
        self.question_id = question_id
        self.answer = answer
        self.save()
        return self

    def load_answer(self, questionnaire_id, question_id):
        """ Load and return the answer for the passed-in ids """
        try:
            existing_answer = Answer.objects.get(
                questionnaire_id=questionnaire_id, question_id=question_id)
        except:
            existing_answer = None
        return existing_answer

    def __str__(self):
        question_id_answer = str(self.question_id) + '/' + str(self.answer)
        return question_id_answer
