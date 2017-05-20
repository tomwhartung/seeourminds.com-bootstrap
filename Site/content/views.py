""" views.py for our content app

Purpose: define the views for this app
Author: Tom W. Hartung
Date: Winter, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none)
"""

import json
import os
import textwrap

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.views.generic.base import View

from .adsense import adsense_ads
from .database import Questionnaire
from .forms import QuestionnaireForm
from .models import Gallery, Image, Score


def home(request):

    """ Load and render the Home page template """

    quiz_menu_data = Questionnaire.get_quiz_menu_data()
    template = loader.get_template('content/home.html')
    context = {
        'adsense_ads': adsense_ads,
        'quiz_menu_data': quiz_menu_data,
    }
    return HttpResponse(template.render(context, request))


def image(request, gallery_name=None, image_id=None):

    """ Render the single image template """

    this_image = Image(gallery_name, image_id)
    image_dict = this_image.image_dict
    quiz_menu_data = Questionnaire.get_quiz_menu_data()
    return render(request, 'content/image.html', {
        'image_dict': image_dict,
        'adsense_ads': adsense_ads,
        'quiz_menu_data': quiz_menu_data,
    })


def galleries(request):

    """
    Load and render the template displaying the list of Galleries
    Note that this page is hard coded, so we pass in
    only the data all pages need, for the ads and the menu.
    """

    quiz_menu_data = Questionnaire.get_quiz_menu_data()
    template = loader.get_template('content/galleries_list.html')
    context = {
        'adsense_ads': adsense_ads,
        'quiz_menu_data': quiz_menu_data,
    }
    return HttpResponse(template.render(context, request))


def gallery(request, gallery_name='None'):

    """ Load and render the template for a single Gallery page """

    if gallery_name == 'None':
        gallery_name = 'generic'

    this_gallery = Gallery(gallery_name)
    this_gallery.set_image_link_values()
    gallery_dict = this_gallery.gallery_dict

    quiz_menu_data = Questionnaire.get_quiz_menu_data()
    template = loader.get_template('content/galleries_gallery.html')
    context = {
        'gallery_dict': gallery_dict,
        'adsense_ads': adsense_ads,
        'quiz_menu_data': quiz_menu_data,
    }
    return HttpResponse(template.render(context, request))


def quiz_about(request):

    """ Load and render the quiz_about page template """

    quiz_info = {}
    quiz_info["quiz_size_abbr"] = ''
    quiz_info["question_count"] = 0
    quiz_info["size_text"] = ''

    quiz_list_data = Questionnaire.get_quiz_list_data()
    quiz_menu_data = Questionnaire.get_quiz_menu_data()
    template = loader.get_template('content/quiz_about.html')
    context = {
        'quiz_info': quiz_info,
        'quiz_menu_data': quiz_menu_data,
        'adsense_ads': adsense_ads,
        'quiz_list_data': quiz_list_data,
    }
    return HttpResponse(template.render(context, request))


def quiz_form(request, quiz_size_slug=Questionnaire.DEFAULT_QUIZ_SIZE_SLUG):

    """ Load and render the quiz_form page template """

    quiz_menu_data = Questionnaire.get_quiz_menu_data()
    quiz_form = None
    if request.method == 'POST':
        # print('views.quiz() - request.POST:', request.POST)
        try:
            email = request.POST["email"]
            load_answers = request.POST["load-answers"]
        except:
            email = ''
            load_answers = ''
        if "Load" in load_answers:
            if email == '':
                need_email_msg = 'ERROR: you must enter a valid ' + \
                    'email address to load the answers'
                messages.add_message(request, messages.ERROR, need_email_msg)
            else:
                questionnaire = Questionnaire()
                new_request_data = questionnaire.add_answers(email, request)
                # print('views.quiz() - new_request_data:', new_request_data)
                quiz_form = QuestionnaireForm(
                        quiz_size_slug=quiz_size_slug, data=new_request_data)
        else:  # Not loading answers, this is a questionnaire form submission
            quiz_form = QuestionnaireForm(
                    quiz_size_slug=quiz_size_slug, data=request.POST)
            if quiz_form.is_valid():
                # print('views.quiz() - quiz_form is_valid')
                score = Score()
                score.score_quiz(quiz_size_slug, quiz_form.cleaned_data)
                if score.is_complete():
                    # print('views.quiz() - score is_complete')
                    saved_messages = score.save_questionnaire(
                            quiz_form.cleaned_data, quiz_size_slug)
                    score.set_quiz_results_messages(request)
                    for saved_msg in saved_messages:
                        messages.add_message(request, messages.INFO, saved_msg)
                    template = loader.get_template('content/quiz_results.html')
                    score_for_context = score.as_list_of_pairs()
                    context = {'score': score_for_context, 'quiz_menu_data': quiz_menu_data,}
                    response = HttpResponse(template.render(context, request))
                    # return HttpResponseRedirect('/quiz/results')
                    return response
                else:
                    score.set_incomplete_message(request)

    if quiz_form == None:
        quiz_form = QuestionnaireForm(quiz_size_slug=quiz_size_slug)

    quiz_info = {}
    quiz_info["quiz_size_slug"] = quiz_size_slug
    quiz_info["quiz_size_abbr"] = \
        Questionnaire.get_quiz_size_abbr_for_slug(quiz_size_slug)
    quiz_info["question_count"] = \
        Questionnaire.get_question_count_for_slug(quiz_size_slug)
    quiz_info["size_text"] = \
        Questionnaire.get_quiz_size_text_for_slug(quiz_size_slug)

    template = loader.get_template('content/quiz_form.html')
    context = {
        'quiz_form': quiz_form,
        'quiz_info': quiz_info,
        'adsense_ads': adsense_ads,
        'quiz_menu_data': quiz_menu_data,
    }
    return HttpResponse(template.render(context, request))


def google_verification(request):

    """ Load and render the google verification template """

    template = loader.get_template('content/google428ef5aab2bc0870.html')
    context = {}
    return HttpResponse(template.render(context, request))
