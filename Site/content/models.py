""" Contains the non-database models for our app.

Purpose: contains the models for unsaved data and read-only data in json format
Author: Tom W. Hartung
Date: Winter, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none, yet)
"""

import json
import os
from django.contrib import messages

from .database import Questionnaire

DJANGO_DEBUG = os.environ.get('DJANGO_DEBUG')


class Score:

    """ Class to calculate, contain, and display the score for the quiz """

    def __init__(self):
        self.score_is_complete = False
        self.unanswered_question_count = -1
        self.e_score = 0
        self.i_score = 0
        self.n_score = 0
        self.s_score = 0
        self.f_score = 0
        self.t_score = 0
        self.j_score = 0
        self.p_score = 0
        self.opposite_type = {
                "E": "I", "I": "E",
                "N": "S", "S": "N",
                "F": "T", "T": "F",
                "J": "P", "P": "J",
        }
        self.e_pct = None
        self.i_pct = None
        self.n_pct = None
        self.s_pct = None
        self.f_pct = None
        self.t_pct = None
        self.j_pct = None
        self.p_pct = None

    def score_quiz(self, quiz_size_slug, cleaned_data):

        """ Process the data from the form and set the scores """
        """ question_list is 0 based, the form questions are 1-based """

        # self.print_cleaned_data(cleaned_data)
        questions = Questions()
        questions_in_form = Questionnaire.get_question_count_for_slug(quiz_size_slug)
        questions_answered = 0

        for form_question_str in sorted(cleaned_data):
            if not form_question_str.startswith("question_"):
                continue
            question_int = int(form_question_str.replace("question_", ""))
            answer_123_type = questions.get_answer_123_type(question_int)
            answer_str = cleaned_data[form_question_str]
            if len(answer_str) > 0:
                answer_int = int(answer_str)
                answer_weight_str = questions.get_answer_weight(question_int, answer_str)
                answer_weight_int = int(answer_weight_str)
                self.tally_answer(answer_123_type, answer_int, answer_weight_int)
                questions_answered += 1
                if DJANGO_DEBUG:
                    answer_text = questions.get_answer_text(question_int, answer_str)
                    question_text = questions.get_question_text(question_int)
                    print('Score.score_quiz -',
                        str(question_int) + ' (' + answer_123_type + ')', '/',
                        str(answer_int) + ' (' + answer_weight_str + ')',
                        question_text, '/',
                        answer_text)

        if DJANGO_DEBUG:
            print('Score - score_quiz: questions_answered/questions_in_form',
                    str(questions_answered) + '/' + str(questions_in_form))

        self.unanswered_question_count = questions_in_form - questions_answered
        if self.unanswered_question_count == 0:
            self.score_is_complete = True
        return self

    def save_questionnaire(self, cleaned_data, quiz_size_slug):
        """
        If we have an email address, save the questionnaire to the db
        (It's a tiny method, but we want to keep logic in the view to a minimum)
        """
        email = cleaned_data["email"]
        saved_messages = []

        if email == '':
            saved_messages.append('You did not share your email address, ' + \
                'so your answers were not saved on the server.')
            saved_messages.append('If you want to save these results, ' + \
                'you need to write them down.')
        else:
            # print( 'Score - save_questionnaire: saving quiz for "' + email + '"')
            questionnaire = Questionnaire()
            questionnaire.save_questionnaire(cleaned_data, quiz_size_slug)
            question_count = questionnaire.get_question_count_for_slug(quiz_size_slug)
            saved_messages.append('Your questionnaire, including your ' + \
                str(question_count) + ' answers, are saved on the server!')
            saved_messages.append('You can use your email (' + email + ') ' + \
                'to retrieve them at any time.')

        return saved_messages


    def print_cleaned_data(self, cleaned_data):
        """ print out the cleaned data, in order by question number """
        print('Score.print_cleaned_data - cleaned_data:')

        for question_xx in sorted(cleaned_data):
            print('\tanswer for ' + question_xx + ': ' + cleaned_data[question_xx])

    def tally_answer(self, answer_123_type, answer_int, answer_weight_int):

        """ Add the answer_weight to the appropriate score data member """

        if answer_int <= 3:
            type_for_answer = answer_123_type
        else:
            type_for_answer = self.opposite_type[answer_123_type]

        if type_for_answer is "E":
            self.e_score += answer_weight_int
        elif type_for_answer is "I":
            self.i_score += answer_weight_int
        elif type_for_answer is "N":
            self.n_score += answer_weight_int
        elif type_for_answer is "S":
            self.s_score += answer_weight_int
        elif type_for_answer is "F":
            self.f_score += answer_weight_int
        elif type_for_answer is "T":
            self.t_score += answer_weight_int
        elif type_for_answer is "J":
            self.j_score += answer_weight_int
        elif type_for_answer is "P":
            self.p_score += answer_weight_int

        if DJANGO_DEBUG:
            print('Score.tally_answer - added',
                str(answer_weight_int) + ' to '+ type_for_answer + ': ',
                self.__str__())
        return True

    def is_complete(self):
        return self.score_is_complete

    def set_incomplete_message(self, request):
        if self.unanswered_question_count == 1:
            incomplete_msg = 'There is ' + \
                str(self.unanswered_question_count) + ' unanswered question'
        else:
            incomplete_msg = 'There are ' + \
                str(self.unanswered_question_count) + ' unanswered questions'
        messages.add_message(request, messages.ERROR, incomplete_msg)
        return True

    def set_quiz_results_messages(self, request):
        """ Set the messages we display on the results page """
        four_letter_type = "Type: " + self.as_four_letter_type()
        pcts_and_counts_html = self.get_pcts_and_counts_html()
        messages.add_message(request, messages.INFO, four_letter_type)
        messages.add_message(request, messages.INFO, pcts_and_counts_html)
        return True

    def as_four_letter_type(self):
        """ Return a string containing the four letter type """
        four_letter_type = ''

        if self.i_score < self.e_score:
            four_letter_type += 'E'
        elif self.i_score == self.e_score:
            four_letter_type += 'X'
        else:
            four_letter_type += 'I'

        if self.s_score < self.n_score:
            four_letter_type += 'N'
        elif self.s_score == self.n_score:
            four_letter_type += 'X'
        else:
            four_letter_type += 'S'

        if self.t_score < self.f_score:
            four_letter_type += 'F'
        elif self.t_score == self.f_score:
            four_letter_type += 'X'
        else:
            four_letter_type += 'T'

        if self.p_score < self.j_score:
            four_letter_type += 'J'
        elif self.p_score == self.j_score:
            four_letter_type += 'X'
        else:
            four_letter_type += 'P'

        return four_letter_type

    def get_pcts_and_counts_html(self):
        """ Return an html string containing the score's percents and counts """
        score_list = self.as_list_of_pcts_and_counts()
        pcts_and_counts_html = '<ul>'
        for score_pair in score_list:
            pcts_and_counts_html += '<li>'
            for single_score in score_pair:
                pcts_and_counts_html += single_score + '&nbsp;'
            pcts_and_counts_html += '</li>'
        pcts_and_counts_html += '</ul>'
        return pcts_and_counts_html

    def calculate_percentages(self):
        """ Calculate the percentages """
        total_ei_score = self.e_score + self.i_score
        total_ns_score = self.n_score + self.s_score
        total_ft_score = self.f_score + self.t_score
        total_jp_score = self.j_score + self.p_score

        if total_ei_score > 0:
            self.e_pct = round(100 * self.e_score / total_ei_score)
            self.i_pct = round(100 * self.i_score / total_ei_score)
        else:
            self.e_pct = 0
            self.i_pct = 0

        if total_ns_score > 0:
            self.n_pct = round(100 * self.n_score / total_ns_score)
            self.s_pct = round(100 * self.s_score / total_ns_score)
        else:
            self.n_pct = 0
            self.s_pct = 0

        if total_ft_score > 0:
            self.f_pct = round(100 * self.f_score / total_ft_score)
            self.t_pct = round(100 * self.t_score / total_ft_score)
        else:
            self.f_pct = 0
            self.t_pct = 0

        if total_jp_score > 0:
            self.j_pct = round(100 * self.j_score / total_jp_score)
            self.p_pct = round(100 * self.p_score / total_jp_score)
        else:
            self.j_pct = 0
            self.p_pct = 0

    def as_list_of_pcts_and_counts(self):
        """ Return a list containing both percentages and counts """
        if self.e_pct is None:
            self.calculate_percentages()

        score_list = [
            ['E: ' + str(self.e_pct) + '%&nbsp;(' + str(self.e_score) + ')',
             'I: ' + str(self.i_pct) + '%&nbsp;(' + str(self.i_score) + ')'],
            ['N: ' + str(self.n_pct) + '%&nbsp;(' + str(self.n_score) + ')',
             'S: ' + str(self.s_pct) + '%&nbsp;(' + str(self.s_score) + ')'],
            ['F: ' + str(self.f_pct) + '%&nbsp;(' + str(self.f_score) + ')',
             'T: ' + str(self.t_pct) + '%&nbsp;(' + str(self.t_score) + ')'],
            ['J: ' + str(self.j_pct) + '%&nbsp;(' + str(self.j_score) + ')',
             'P: ' + str(self.p_pct) + '%&nbsp;(' + str(self.p_score) + ')']
        ]
        return score_list

    def to_kv_pairs(self):
        """ Returns the current score as a list of key-value pairs """
        score = {
                "E": self.e_score,
                "I": self.i_score,
                "N": self.n_score,
                "S": self.s_score,
                "F": self.f_score,
                "T": self.t_score,
                "J": self.j_score,
                "P": self.p_score,
        }
        return score

    #
    # Reference for purpose of __str__() and __repl__():
    #   http://stackoverflow.com/questions/3691101/what-is-the-purpose-of-str-and-repr-in-python
    #

    def __repl__(self):
        return str(self.to_kv_pairs())

    def __str__(self):
        score_str  = 'E/I: ' + str(self.e_score) + '/' + str(self.i_score) + '; '
        score_str += 'N/S: ' + str(self.n_score) + '/' + str(self.s_score) + '; '
        score_str += 'F/T: ' + str(self.f_score) + '/' + str(self.t_score) + '; '
        score_str += 'J/P: ' + str(self.j_score) + '/' + str(self.p_score)
        return score_str


class Questions:

    """ Read in and work with all the questions in the entire quiz """


    def __init__(self):

        """ Populate the question_list with questions from the json file """

        self.question_list = self.read_quiz_json()

    def read_quiz_json(self):

        """ Read the quiz questions and answers from the json file """

        site_content_dir = os.path.abspath(os.path.dirname(__file__))
        QUIZ_FILE_DIR = site_content_dir + '/static/content/json/quiz/'
        QUIZ_FILE_NAME = 'seeourminds_quiz.json'

        quiz_file_path = QUIZ_FILE_DIR + QUIZ_FILE_NAME
        quiz_json_file = open(quiz_file_path)
        quiz_json_string = quiz_json_file.read()
        quiz_json_file.close()
        question_list = json.loads(quiz_json_string)
        return(question_list)

    def get_quiz_question(self, question_int):

        """ Return the entire quiz question (answers, weights, etc.)"""

        quiz_question = self.question_list[question_int]
        # print('Questions.get_quiz_question - question_int:', question_int)
        # print('Questions.get_quiz_question - quiz_question:', quiz_question)
        return quiz_question

    def get_question_text(self, question_int):

        """ Get and return the question_text for the question """

        quiz_question = self.get_quiz_question(question_int)
        question_text = quiz_question['question_text']
        return question_text

    def get_choices(self, question_int):

        """ Return the answer choices for the given question """

        quiz_question = self.get_quiz_question(question_int)
        choices = []

        if len(quiz_question['answer_1_text']) > 0 and \
           int(quiz_question['answer_1_weight']) > 0:
            choice_1 = ['1', quiz_question['answer_1_text']]
            choices.append(choice_1)

        if len(quiz_question['answer_2_text']) > 0 and \
           int(quiz_question['answer_2_weight']) > 0:
            choice_2 = ['2', quiz_question['answer_2_text']]
            choices.append(choice_2)

        if len(quiz_question['answer_3_text']) > 0 and \
           int(quiz_question['answer_3_weight']) > 0:
            choice_3 = ['3', quiz_question['answer_3_text']]
            choices.append(choice_3)

        if len(quiz_question['answer_4_text']) > 0 and \
           int(quiz_question['answer_4_weight']) > 0:
            choice_4 = ['4', quiz_question['answer_4_text']]
            choices.append(choice_4)

        if len(quiz_question['answer_5_text']) > 0 and \
           int(quiz_question['answer_5_weight']) > 0:
            choice_5 = ['5', quiz_question['answer_5_text']]
            choices.append(choice_5)

        if len(quiz_question['answer_6_text']) > 0 and \
           int(quiz_question['answer_6_weight']) > 0:
            choice_6 = ['6', quiz_question['answer_6_text']]
            choices.append(choice_6)

        answer_7_text = quiz_question.get('answer_7_text')
        # print("answer_7_text:", answer_7_text)

        if answer_7_text is not None:
            choice_7 = ['7', answer_7_text]
            choices.append(choice_7)

        # print('Questions.get_choices - question_int:', question_int)
        # print('Questions.get_choices - len(choices):', len(choices))
        return choices

    def get_answer_123_type(self, question_int):

        """ Get and return the answer_123_type (e.g., "E") for the question """

        quiz_question = self.get_quiz_question(question_int)
        answer_123_type = quiz_question['answer_123_type']
        return answer_123_type

    def get_answer_text(self, question_int, answer_str):

        """ Get and return the answer_X_text for the selected answer 'X' """

        quiz_question = self.get_quiz_question(question_int)
        answer_text_key = "answer_" + answer_str + "_text"
        answer_text = quiz_question[answer_text_key]
        return answer_text

    def get_answer_weight(self, question_int, answer_str):

        """ Get and return the answer_X_weight for the selected answer 'X' """

        quiz_question = self.get_quiz_question(question_int)
        answer_weight_key = "answer_" + answer_str + "_weight"
        answer_weight = quiz_question[answer_weight_key]
        return answer_weight
