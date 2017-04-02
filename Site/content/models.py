""" Contains the models for our app.

Purpose: just because we aren't using a db doesn't mean we can't have models
Author: Tom W. Hartung
Date: Winter, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none, yet)
"""

import json
import os
from django.db import models

site_content_dir = os.path.abspath(os.path.dirname(__file__))
QUIZ_FILE_DIR = site_content_dir + '/static/content/json/quiz/'
QUIZ_FILE_NAME = 'seeourminds_quiz.json'


class Score(models.Model):

    """ Class to contain the score for the quiz """

    def __init__(self):
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

    def tally_answer(self, answer_123_type, answer_selected_int, answer_weight_int):

        """ Add the answer_weight to the appropriate score data member """

        if answer_selected_int <= 3:
            type_for_answer = answer_123_type
        else:
            type_for_answer = self.opposite_type[answer_123_type]

        # print('Score.tally_answer - answer_123_type:', answer_123_type)
        # print('Score.tally_answer - answer_selected_int:', answer_selected_int)
        # print('Score.tally_answer - answer_weight_int:', answer_weight_int)
        # print('Score.tally_answer - type_for_answer:', type_for_answer)

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

        print('Score.tally_answer -',
                'adding', answer_weight_int, 'to', type_for_answer)
        print('Score.tally_answer - self.__str__():',  self.__str__())

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

    def calculate_percentages(self):
        """ Calculate the percentages """
        self.e_pct = round(100 * self.e_score / (self.e_score + self.i_score))
        self.i_pct = round(100 * self.i_score / (self.e_score + self.i_score))
        self.n_pct = round(100 * self.n_score / (self.n_score + self.s_score))
        self.s_pct = round(100 * self.s_score / (self.n_score + self.s_score))
        self.f_pct = round(100 * self.f_score / (self.f_score + self.t_score))
        self.t_pct = round(100 * self.t_score / (self.f_score + self.t_score))
        self.j_pct = round(100 * self.j_score / (self.j_score + self.p_score))
        self.p_pct = round(100 * self.p_score / (self.j_score + self.p_score))

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

    def as_list_of_counts_and_pcts(self):
        """ Return a list containing both counts and percentages """
        if self.e_pct is None:
            self.calculate_percentages()

        score_list = [
            ['E: ' + str(self.e_score) + '(' + str(self.e_pct) + '%)',
             'I: ' + str(self.i_score) + '(' + str(self.i_pct) + '%)'],
            ['N: ' + str(self.n_score) + '(' + str(self.n_pct) + '%)',
             'S: ' + str(self.s_score) + '(' + str(self.s_pct) + '%)'],
            ['F: ' + str(self.f_score) + '(' + str(self.f_pct) + '%)',
             'T: ' + str(self.t_score) + '(' + str(self.t_pct) + '%)'],
            ['J: ' + str(self.j_score) + '(' + str(self.j_pct) + '%)',
             'P: ' + str(self.p_score) + '(' + str(self.p_pct) + '%)']
        ]
        return score_list

    def as_percentages(self):
        """ Return a string containing the percentages """
        if self.e_pct is None:
            self.calculate_percentages()

        score_str  = 'E/I: ' + str(self.e_pct) + '%/' + str(self.i_pct) + '%; '
        score_str += 'N/S: ' + str(self.n_pct) + '%/' + str(self.s_pct) + '%; '
        score_str += 'F/T: ' + str(self.f_pct) + '%/' + str(self.t_pct) + '%; '
        score_str += 'J/P: ' + str(self.j_pct) + '%/' + str(self.p_pct) + '%'
        return score_str

    def as_counts_and_pcts(self):
        """ Return a string containing both counts and percentages """
        if self.e_pct is None:
            self.calculate_percentages()

        score_str  = 'E: ' + str(self.e_score) + '(' + str(self.e_pct) + '%)/'
        score_str += 'I: ' + str(self.i_score) + '(' + str(self.i_pct) + '%) - '
        score_str += 'N: ' + str(self.n_score) + '(' + str(self.n_pct) + '%)/'
        score_str += 'S: ' + str(self.s_score) + '(' + str(self.s_pct) + '%) - '
        score_str += 'F: ' + str(self.f_score) + '(' + str(self.f_pct) + '%)/'
        score_str += 'T: ' + str(self.t_score) + '(' + str(self.t_pct) + '%) - '
        score_str += 'J: ' + str(self.j_score) + '(' + str(self.j_pct) + '%)/'
        score_str += 'P: ' + str(self.p_score) + '(' + str(self.p_pct) + '%)'
        return score_str

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

    #
    # Crufty function(s) we wrote once but no longer use but may be useful
    #

    def to_list_of_lists(self):
        """ Returns the current score as a list of lists """
        score = [
                ["E", self.e_score],
                ["I", self.i_score],
                ["N", self.n_score],
                ["S", self.s_score],
                ["F", self.f_score],
                ["T", self.t_score],
                ["J", self.j_score],
                ["P", self.p_score],
        ]
        return score


class Quiz(models.Model):

    """ Model all the questions in the entire quiz """

    def __init__(self):

        """ Populate the question_list with questions from the json file """

        self.question_list = self.read_quiz_json()

    def read_quiz_json(self):

        """ Read the quiz questions and answers from the json file """

        quiz_file_path = QUIZ_FILE_DIR + QUIZ_FILE_NAME
        quiz_json_file = open(quiz_file_path)
        quiz_json_string = quiz_json_file.read()
        quiz_json_file.close()
        question_list = json.loads(quiz_json_string)
        return(question_list)

    def get_quiz_question(self, list_question_int):

        """ Return the entire quiz question (answers, weights, etc.)"""

        quiz_question = self.question_list[list_question_int]
        # print('Quiz.get_quiz_question - list_question_int:', list_question_int)
        # print('Quiz.get_quiz_question - quiz_question:', quiz_question)
        return quiz_question

    def get_label(self, list_question_int):

        """ Get and return the question_text ("label") for the question """
        """ list_question_int is 0 based, the question ids and labels are 1-based """

        quiz_question = self.get_quiz_question(list_question_int)
        form_question_int = list_question_int + 1
        label = str(form_question_int) + '. ' + quiz_question['question_text']
        # print('Quiz.get_label - list_question_int:', list_question_int)
        # print('Quiz.get_label - label:', label)
        return label

    def get_choices(self, list_question_int):

        """ Return the answer choices for the given question """

        quiz_question = self.get_quiz_question(list_question_int)
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

        # print('Quiz.get_choices - list_question_int:', list_question_int)
        # print('Quiz.get_choices - len(choices):', len(choices))
        return choices

    def get_answer_123_type(self, list_question_int):

        """ Get and return the answer_123_type (e.g., "E") for the question """

        quiz_question = self.get_quiz_question(list_question_int)
        answer_123_type = quiz_question['answer_123_type']
        return answer_123_type

    def get_answer_text(self, list_question_int, answer_selected_str):

        """ Get and return the answer_X_text for the selected answer 'X' """

        quiz_question = self.get_quiz_question(list_question_int)
        answer_text_key = "answer_" + answer_selected_str + "_text"
        answer_text = quiz_question[answer_text_key]
        return answer_text

    def get_answer_weight(self, list_question_int, answer_selected_str):

        """ Get and return the answer_X_weight for the selected answer 'X' """

        quiz_question = self.get_quiz_question(list_question_int)
        answer_weight_key = "answer_" + answer_selected_str + "_weight"
        answer_weight = quiz_question[answer_weight_key]
        return answer_weight

    def print_cleaned_data(self, cleaned_data):
        """ print out the cleaned data, in order by question number """
        print('Quiz.print_cleaned_data - cleaned_data:')

        for question_xx in sorted(cleaned_data):
            print('\tanswer for ' + question_xx + ': ' + cleaned_data[question_xx])

    def score_quiz(self, cleaned_data):

        """ Process the data from the form and set the scores """
        """ question_list is 0 based, the form questions are 1-based """

        # self.print_cleaned_data(cleaned_data)
        score = Score()

        for form_question_str in sorted(cleaned_data):
            form_question_int = int(form_question_str.replace("question_", ""))
            list_question_int = int(form_question_int) - 1
            answer_123_type = self.get_answer_123_type(list_question_int)
            answer_selected_str = cleaned_data[form_question_str]
            answer_selected_int = int(answer_selected_str)
            answer_text = self.get_answer_text(list_question_int, answer_selected_str)
            answer_weight_str = self.get_answer_weight(list_question_int, answer_selected_str)
            answer_weight_int = int(answer_weight_str)

            # print('Quiz.score_quiz - form_question_str:',  str(form_question_str))
            # print('Quiz.score_quiz - form_question_int:', str(form_question_int))
            # print('Quiz.score_quiz - list_question_int:', str(list_question_int))
            # print('Quiz.score_quiz - answer_123_type:',  answer_123_type)
            # print('Quiz.score_quiz - answer_selected_str:',  answer_selected_str)
            # print('Quiz.score_quiz - answer_selected_int:', answer_selected_int)
            # print('Quiz.score_quiz - answer_text:',  answer_text)
            # print('Quiz.score_quiz - answer_weight_str:',  answer_weight_str)
            # print('Quiz.score_quiz - answer_weight_int:',  answer_weight_int)
            # print('Quiz.score_quiz - score:',  score)

            print('Quiz.score_quiz -',
                    'question: ' + str(form_question_int) + ',',
                    'type: ' + answer_123_type + ', ',
                    'answer: ' + str(answer_selected_int))

            score.tally_answer(answer_123_type, answer_selected_int, answer_weight_int)

        return score
