""" Contains the non-database models for our app.

Purpose: contains the models for unsaved data and read-only data in json format
Author: Tom W. Hartung
Date: Winter, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none, yet)
"""

import fnmatch
import json
import os
import random
from django.contrib import messages
from django.http import HttpResponse

from .database import Questionnaire

DJANGO_DEBUG = os.environ.get('DJANGO_DEBUG')


class GalleriesList:

    """
    Read in the gallery files appropriate for the (optional) specified
    galleries_list_name and support listing them on a single page
    """

    title_dict = {
        'cheers': 'Cheers',
        'deadwood': 'Deadwood',
        'experiments': 'Experimental Compositions',
        'famous': 'Famous',
        'family': 'Family',
        'fictional': 'Fictional',
        'friends': 'Friends',
        'game_of_thrones': 'Game of Thrones',
        'movies': 'Movies',
        'others': 'Other People I Know',
        'politicians': 'American Politicians',
        'presidents': 'American Presidents',
        'real': 'Real',
        'sixteen_types': 'Sixteen Types',
        'star_wars': 'Star Wars',
        'the_wire': 'The Wire',
        'true_detective': 'True Detective',
        'twin_peaks': 'Twin Peaks',
        'tv': 'TV Shows',
    }
    fnmatch_string_dict = {
        'cheers': '[0-9]*-cheers-*',
        'deadwood': '[0-9]*-deadwood-*',
        'experiments': '[0-9]*-experiments-*',
        'family': '[0-9]*-family-*',
        'famous': '[0-9]*-famous*',
        'fictional': '[0-9]*-fictional*',
        'friends': '[0-9]*-friends-*',
        'game_of_thrones': '[0-9]*-game_of_thrones-*',
        'movies': '[0-9]*-movies-*',
        'others': '[0-9]*-others-*',
        'politicians': '[0-9]*-politicians-*',
        'presidents': '[0-9]*-politicians-us_presidents*',
        'real': '[0-9]*-real*',
        'sixteen_types': '[0-9]*generic_images*',
        'star_wars': '[0-9]*-star_wars-*',
        'the_wire': '[0-9]*-the_wire-*',
        'true_detective': '[0-9]*-true_detective-*',
        'tv': '[0-9]*-tv-*',
        'twin_peaks': '[0-9]*-twin_peaks-*',
    }
    phrase_dict = {
        'cheers': 'images of characters from <b>Cheers:</b>',
        'deadwood': 'images of characters from <b>Deadwood:</b>',
        'experiments': '<b>experimental</b> images:',
        'family': 'images of <b>people in my family:</b>',
        'famous': 'images of <b>famous</b> people:',
        'fictional': 'images of <b>fictional</b> people, from movies, etc.:',
        'friends': 'images of <b>some of my friends:</b>',
        'game_of_thrones': 'images of characters in <b>Game of Thrones:</b>',
        'movies': 'images of characters in <b>movies:</b>',
        'others': 'images of <b>other real people I know:</b>',
        'politicians': 'images of American politicians:',
        'presidents': 'images of American Presidents:',
        'real': 'images of <b>real</b> people:',
        'sixteen_types': '<b>generic images:</b>',
        'star_wars': 'images of characters from <b>Star Wars:</b>',
        'the_wire': 'images of characters from <b>The Wire:</b>',
        'true_detective': 'images of characters from <b>True Detective:</b>',
        'tv': 'images of characters from <b>tv shows:</b>',
        'twin_peaks': 'images of characters from <b>Twin Peaks:</b>',
    }
    list_contains_lists = [
        'all', 'fictional', 'movies', 'tv'
    ]
    """ Shows that contain multiple galleries require special handling """
    contains_mult_gals = [
        'cheers',
        'deadwood',
        'game_of_thrones',
        'star_wars',
        'the_wire',
        'true_detective',
        'twin_peaks',
    ]
    GALLERIES_DIRECTORY = '/static/content/json/galleries/'
    LIST_PAGE_TEXT_INTRO_LENGTH = 60

    def __init__(self, galleries_list_name='all'):

        """ Read in all the json for the passed-in galleries_list_name """

        self.first_file_included = {}
        for series in self.contains_mult_gals:
            self.first_file_included[series] = False

        site_content_dir = os.path.abspath(os.path.dirname(__file__))
        galleries_root_dir = site_content_dir + self.GALLERIES_DIRECTORY
        gallery_files = sorted(os.listdir(galleries_root_dir))
        phrase = 'these galleries, containing '

        if self.title_dict.get(galleries_list_name):
            self.galleries_list_title = self.title_dict.get(galleries_list_name)
            phrase += self.phrase_dict.get(galleries_list_name)
        else: # default: get all galleries
            galleries_list_name = 'all'
            self.galleries_list_title = 'All Galleries'
            phrase = '<b>all</b> available galleries!'

        self.galleries_list_name = galleries_list_name
        self.descriptive_phrase_html = phrase
        self.gallery_files = []

        for gal_file in gallery_files:
            if self.include_in_gallery_list(gal_file):
                self.gallery_files.append(gal_file)
                if DJANGO_DEBUG:
                    print('GalleriesList - __init__ using gal_file:', gal_file)

        if DJANGO_DEBUG:
            print('GalleriesList - __init__ - galleries_list_name:', galleries_list_name)
            print('GalleriesList - __init__ - self.gallery_files:', self.gallery_files)

        self.galleries_list_data = []


    def include_in_gallery_list(self, gal_file):
        """
        Determine whether to include gal_file in the list
        """
        galleries_list_name = self.galleries_list_name
        if self.fnmatch_string_dict.get(galleries_list_name):
            fnmatch_string = self.fnmatch_string_dict.get(galleries_list_name)
        else: # default: get all galleries - already checked in __init__ so ...
            fnmatch_string = '[0-9]*'

        #print('include_in_gallery_list - galleries_list_name:', galleries_list_name)
        #print('include_in_gallery_list - fnmatch_string:', '"' + fnmatch_string + '"')
        include_this_file = False
        #
        # Lists that contain lists require special handling:
        #   When displaying a list that contains lists - such as 'all' and 'tv',
        #       When listing a show with multiple galleries, e.g., cheers
        #          we want to include only the first one
        # More specifically:
        #   When listing a single show's galleries explicitly,
        #       include all file name matches
        #   else
        #       include only the first one
        #       use the gallery_group_title and gallery_group_page
        #
        if fnmatch.fnmatch(gal_file, fnmatch_string):
            #print('include_in_gallery_list - gal_file matches:', gal_file)
            if self.galleries_list_name in self.list_contains_lists:
                for first_incl_key in self.first_file_included.keys():
                    str_to_match = self.fnmatch_string_dict.get(first_incl_key)
                    if fnmatch.fnmatch(gal_file, str_to_match):
                        first_incl = self.first_file_included.get(first_incl_key)
                        #print('include_in_gallery_list - gal_file matches:', gal_file)
                        #print('include_in_gallery_list - first_incl:', first_incl)
                        if first_incl:
                            #print('include_in_gallery_list - rejecting gal_file, not the first')
                            include_this_file = False
                        else:
                            #print('include_in_gallery_list - including first_only gal_file')
                            include_this_file = True
                            self.first_file_included[first_incl_key] = True
                        break
                    else:
                        include_this_file = True
            else:
                #print('include_in_gallery_list - not a list of lists, using gal_file:', gal_file)
                include_this_file = True
        else:
            #print('include_in_gallery_list - no match, gal_file rejected:', gal_file)
            include_this_file = False

        return include_this_file


    def set_galleries_list_data(self):
        """
        Get the data needed for the galleries list page
        Show ads randomly intermingled with the galleries, but NOT two in a row
        Note: Called from the view
        """

        ad_added_last_time = False
        for gal_file in self.gallery_files:
            gal_file_name, gal_file_ext = os.path.splitext(gal_file)
            this_gallery = Gallery(gal_file_name)
            this_gallery.set_image_link_values()
            this_gallery.set_gallery_image_dictionary()
            gallery_dict = this_gallery.gallery_dict
            gallery_dict['gallery_file_name'] = gal_file_name
            gallery_group_title = gallery_dict.get('gallery_group_title')
            gallery_group_page = gallery_dict.get('gallery_group_page')
            if gallery_group_title and gallery_group_page:
                if self.galleries_list_name == gallery_group_page:
                    link_to_gallery = '/gallery/' + gal_file_name
                else:
                    gallery_dict['gallery_title'] = gallery_group_title
                    link_to_gallery = '/galleries/' + gallery_group_page
            else:
                link_to_gallery = '/gallery/' + gal_file_name
            gallery_dict['link_to_gallery'] = link_to_gallery
            #print('set_galleries_list_data:')
            #print('gallery_group_title:', gallery_group_title)
            #print('gallery_group_page:', gallery_group_page)
            #print('gallery_dict[gallery_title]:', gallery_dict['gallery_title'])
            #print('link_to_gallery:', link_to_gallery)
            list_page_teaser = gallery_dict['list_page_teaser']
            gallery_dict['list_page_teaser_intro'] \
                = list_page_teaser[:self.LIST_PAGE_TEXT_INTRO_LENGTH]
            gallery_dict['list_page_teaser_remainder'] \
                = list_page_teaser[self.LIST_PAGE_TEXT_INTRO_LENGTH:]
            self.galleries_list_data.append(gallery_dict)
            if ad_added_last_time:   # do NOT show an ad until MAYBE next time
                ad_added_last_time = False
            else:  # MAYBE add an ad, randomly
                random_int_1_2 = random.randint(1,2)
                if random_int_1_2 == 2:
                    gallery_dict = { "gallery_title": "responsive_ad" }
                    self.galleries_list_data.append(gallery_dict)
                    ad_added_last_time = True

        return self.galleries_list_data


class Gallery:

    """ Read in and work with all the images, etc. in a single gallery """

    GALLERY_PAGE_TEXT_INTRO_LENGTH = 60

    def __init__(self, gallery_file_name=None):
        """ Read in all the json for the passed-in gallery_file_name """

        self.gallery_file_name = gallery_file_name
        if gallery_file_name == None:
            self.gallery_dict = {}
        else:
            #print('gallery_file_name:', gallery_file_name)
            data_file_name = gallery_file_name + '.json'
            site_content_dir = os.path.abspath(os.path.dirname(__file__))
            data_file_dir = site_content_dir + GalleriesList.GALLERIES_DIRECTORY
            data_file_path = data_file_dir + data_file_name
            gallery_json_file = open(data_file_path, encoding='utf-8', mode="r")
            gallery_json_string = gallery_json_file.read()
            gallery_json_file.close()
            self.gallery_dict = json.loads(gallery_json_string)


    def find_image(self, image_id=None):
        """ Returns all data from the json for image, or None if not found """

        image_dict = None
        if image_id != None:
            #print('find_image: Looking for image_id = "' + image_id + '"')
            for image_dict in self.gallery_dict["image_list"]:
                if image_dict["id"] == image_id:
                    image_dict = image_dict
                    #print('find_image returning image_dict:', image_dict )
                    break
        return image_dict

    def set_gallery_image_dictionary(self):
        """
        When listing galleries, set image_dict equal to the first image
        If the title indicates it's an "*_ad"
            the image_dict is irrelevant and will be empty
        """

        for image_dict in self.gallery_dict["image_list"]:
            image_title = image_dict.get('title')
            if image_title.find('_ad') == -1:
                self.gallery_dict["image_dict"] = image_dict
                break
        return self

    def set_image_link_values(self):
        """
        Set derived values in the image list in the gallery_dict
        I.e., prepend the derived directory to the image file name
        NOTE: the image_file_directory equals the gallery_file_name!
        """

        image_file_directory = self.gallery_file_name
        image_file_dir = 'content/images/galleries/' \
            + image_file_directory + '/'
        for image_dict in self.gallery_dict['image_list']:
            image_file_name = image_dict.get('image_file_name')
            if image_file_name:
                image_dict['image_file_path'] = image_file_dir \
                    + image_dict['image_file_name']
                image_dict['image_link_href'] = '/image/' \
                    + self.gallery_file_name + '/' + image_dict['id'] + '/'
                image_dict['image_link_title'] = 'Click to see a larger copy of ' \
                    + 'this image on a page with more information about it'
        return self


    def set_image_list_data(self):
        """ Update the raw image list data for display on the gallery page """

        self.set_image_link_values()
        for image_dict in self.gallery_dict['image_list']:
            if image_dict.get("gallery_page_teaser"):
                gallery_page_teaser = image_dict.get("gallery_page_teaser")
                image_dict['gallery_page_teaser_intro'] \
                    = gallery_page_teaser[:self.GALLERY_PAGE_TEXT_INTRO_LENGTH]
                image_dict['gallery_page_teaser_remainder'] \
                    = gallery_page_teaser[self.GALLERY_PAGE_TEXT_INTRO_LENGTH:]
        return self


class Image:

    """ Code for working with images, eg, for single image template """

    IMAGES_DIRECTORY = 'content/images/galleries/'

    def __init__(self, gallery_file_name=None, image_id=None):

        """
        Find image in the json file or use default image
        NOTE: the image_file_directory equals the passed-in gallery_file_name!
        """

        if gallery_file_name == None or image_id == None:
            self.set_default_image_dict()
        else:
            gallery = Gallery(gallery_file_name)
            image_dict = gallery.find_image(image_id)
            if image_dict == None:
                self.set_default_image_dict()
            else:
                self.image_dict = image_dict
                image_file_directory = gallery_file_name
                self.image_dict["path"] = self.IMAGES_DIRECTORY \
                    + image_file_directory + '/' + image_dict["image_file_name"]
                if self.image_dict.get("story_intro_html"):
                    self.image_dict["show_story_btn_text"] \
                        = 'Show the Whole Story'
                else:
                    self.image_dict["show_story_btn_text"] = 'Show the Story'

    def set_default_image_dict(self):
        """ Set self.image_dict data to values used for the default image """

        self.image_dict = {}
        self.image_dict["id"] = 0
        self.image_dict["title"] = 'Tom H., Creator of SeeOurMinds.com and Groja.com'
        self.image_dict["path"] = 'content/images/header/infp-tomh_1987-515x515.gif'
        self.image_dict["score"] = [
            { "e_score": "9", "i_score": "10" },
            { "n_score": "13", "s_score": "6" },
            { "f_score": "10", "t_score": "9" },
            { "j_score": "9", "p_score": "10" }
        ]
        self.image_dict["four_letter_type"] = 'INFP'
        self.image_dict["tweet"] = '"default image tweet - FIX ME"'
        self.image_dict["explanation"] = '"default image explanation - FIX ME"'
        self.image_dict["story"] = 'The image contains mostly blue and red, ' \
           'indicating I am idealistic and passionate.  ' \
           'There is also plenty of green and yellow, however, indicating ' \
           'I can be logical and down-to-earth when the situation calls ' \
           'for it.' \
           'This image is one of someone who is exactly the sort of person ' \
           'who can not just conceive of an idea such as this ' \
           'but also follow through and learn the technical details ' \
           'needed to implement it multiple times and in multiple ' \
           'programming languages.'
        return self

    def set_compare_contrast(self):
        compare_to = self.image_dict.get("compare_to")
        if compare_to:
            gal_fn = compare_to.get("gallery_file_name")
            img_id = compare_to.get("image_id")
            compare_to_image = Image(gal_fn, img_id)
            compare_to_title = compare_to_image.image_dict.get("title")
            compare_to_path = '/image/' + gal_fn + '/' + img_id + '/'
            self.image_dict["compare_to_title"] = compare_to_title
            self.image_dict["compare_to_path"] = compare_to_path
        contrast_with = self.image_dict.get("contrast_with")
        if contrast_with:
            gal_fn = contrast_with.get("gallery_file_name")
            img_id = contrast_with.get("image_id")
            contrast_with_image = Image(gal_fn, img_id)
            contrast_with_title = contrast_with_image.image_dict.get("title")
            contrast_with_path = '/image/' + gal_fn + '/' + img_id + '/'
            self.image_dict["contrast_with_title"] = contrast_with_title
            self.image_dict["contrast_with_path"] = contrast_with_path


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
        quiz_json_file = open(quiz_file_path, encoding='utf-8', mode="r")
        quiz_json_string = quiz_json_file.read()
        quiz_json_file.close()
        question_list = json.loads(quiz_json_string)
        return(question_list)

    def get_quiz_question(self, question_int):

        """ Return the entire quiz question (answers, weights, etc.)"""

        quiz_question = self.question_list[question_int]
        #print('Questions.get_quiz_question - question_int:', question_int)
        #print('Questions.get_quiz_question - quiz_question:', quiz_question)
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
        #print("answer_7_text:", answer_7_text)

        if answer_7_text is not None:
            choice_7 = ['7', answer_7_text]
            choices.append(choice_7)

        #print('Questions.get_choices - question_int:', question_int)
        #print('Questions.get_choices - len(choices):', len(choices))
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
            #print( 'Score - save_questionnaire: saving quiz for "' + email + '"')
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
        """ Returns the boolean data member score_is_complete """
        return self.score_is_complete

    def set_incomplete_message(self, request):
        """ Returns message saying how many questions were not answered """
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

        score_list = []

        if self.e_score > self.i_score:
            e_i_score_list = \
                ['E: ' + str(self.e_pct) + '%&nbsp;(' + str(self.e_score) + ')',
                'I: ' + str(self.i_pct) + '%&nbsp;(' + str(self.i_score) + ')']
        else:
            e_i_score_list = \
                ['I: ' + str(self.i_pct) + '%&nbsp;(' + str(self.i_score) + ')',
                'E: ' + str(self.e_pct) + '%&nbsp;(' + str(self.e_score) + ')']

        if self.e_score > self.i_score:
            n_s_score_list = \
                ['N: ' + str(self.n_pct) + '%&nbsp;(' + str(self.n_score) + ')',
                 'S: ' + str(self.s_pct) + '%&nbsp;(' + str(self.s_score) + ')']
        else:
            n_s_score_list = \
                ['S: ' + str(self.s_pct) + '%&nbsp;(' + str(self.s_score) + ')',
                 'N: ' + str(self.n_pct) + '%&nbsp;(' + str(self.n_score) + ')']

        if self.e_score > self.i_score:
            f_t_score_list = \
                ['F: ' + str(self.f_pct) + '%&nbsp;(' + str(self.f_score) + ')',
                 'T: ' + str(self.t_pct) + '%&nbsp;(' + str(self.t_score) + ')']
        else:
            f_t_score_list = \
                ['T: ' + str(self.t_pct) + '%&nbsp;(' + str(self.t_score) + ')',
                 'F: ' + str(self.f_pct) + '%&nbsp;(' + str(self.f_score) + ')']

        if self.e_score > self.i_score:
            j_p_score_list = \
                ['J: ' + str(self.j_pct) + '%&nbsp;(' + str(self.j_score) + ')',
                 'P: ' + str(self.p_pct) + '%&nbsp;(' + str(self.p_score) + ')']
        else:
            j_p_score_list = \
                ['P: ' + str(self.p_pct) + '%&nbsp;(' + str(self.p_score) + ')',
                 'J: ' + str(self.j_pct) + '%&nbsp;(' + str(self.j_score) + ')']

        score_list.append(e_i_score_list)
        score_list.append(n_s_score_list)
        score_list.append(f_t_score_list)
        score_list.append(j_p_score_list)
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

    def as_list_of_pairs(self):
        """ Return a list of pairs, formatted like the scores in the json """
        score_list = [
            {'e_score': str(self.e_score),
             'i_score': str(self.i_score)},
            {'n_score': str(self.n_score),
             's_score': str(self.s_score)},
            {'f_score': str(self.f_score),
             't_score': str(self.t_score)},
            {'j_score': str(self.j_score),
             'p_score': str(self.p_score)}
        ]
        return score_list

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
