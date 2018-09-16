""" views.py for our content app

Purpose: define the views for this app
Author: Tom W. Hartung
Date: Winter, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none)
"""

import json
import textwrap

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.views.generic.base import View

from .adsense import adsense_ads
from .database import Questionnaire
from .forms import QuestionnaireForm
from .models import GalleriesList, Gallery, Image, Score


def home(request):

    """ Load and render the Home page template """

    template = loader.get_template('content/home.html')
    title = 'SeeOurMinds.com';
    context = {
        'adsense_ads': adsense_ads,
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
        'title': title,
    }
    return HttpResponse(template.render(context, request))


def image(request, gallery_file_name=None, image_id=None):

    """ Render the single image template """

    this_image = Image(gallery_file_name, image_id)
    this_image.set_compare_contrast()
    image_dict = this_image.image_dict
    back_to_gallery_href = '/gallery/' + gallery_file_name + '/'
    title = 'Image: ' + image_dict.get('title')
    return render(request, 'content/image.html', {
        'back_to_gallery_href': back_to_gallery_href,
        'image_dict': image_dict,
        'adsense_ads': adsense_ads,
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
        'title': title,
    })

##
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##   Views for Gallery Pages
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##

def galleries_list(request, galleries_list_name='all'):

    """
    Load and render the template displaying the list of Galleries
        appropriate for the passed-in galleries_list_name
    """

    galleries_list_obj = GalleriesList(galleries_list_name)
    galleries_list_obj.set_galleries_list_data()
    title = galleries_list_obj.galleries_list_title
    template = loader.get_template('content/galleries_list.html')
    context = {
        'galleries_list_obj': galleries_list_obj,
        'adsense_ads': adsense_ads,
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
        'title': title,
    }
    return HttpResponse(template.render(context, request))


def gallery(request, gallery_file_name='None'):

    """ Load and render the template for a single Gallery page """

    if gallery_file_name == 'None':
        gallery_file_name = '0000-generic_images'

    this_gallery = Gallery(gallery_file_name)
    this_gallery.set_image_list_data()
    gallery_dict = this_gallery.gallery_dict
    title = gallery_dict.get('gallery_title')

    template = loader.get_template('content/galleries_gallery.html')
    context = {
        'gallery_dict': gallery_dict,
        'adsense_ads': adsense_ads,
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
        'title': title,
    }
    return HttpResponse(template.render(context, request))

##
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##   Views for Legal Pages
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##

def legal(request):

    """ Load and render the default legal template for this site """

    return terms_of_service(request)


def affiliate_marketing_disclosure(request):

    """ Load and render the affiliate_marketing_disclosure template """

    title = 'Disclosure - ArtsyVisions.com';
    template = 'content/legal/affiliate_marketing_disclosure.html'
    context = {
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
        'title': title,
    }
    return render(request, template, context)


def privacy_policy(request):

    """ Load and render the privacy_policy template """

    title = 'Privacy Policy - ArtsyVisions.com';
    template = 'content/legal/privacy_policy.html'
    context = {
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
        'title': title,
    }
    return render(request, template, context)


def questionnaire_disclaimer(request):

    """ Load and render the questionnaire_disclaimer template """

    title = 'Disclaimer - ArtsyVisions.com';
    template = 'content/legal/questionnaire_disclaimer.html'
    context = {
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
        'title': title,
    }
    return render(request, template, context)


def terms_of_service(request):

    """ Load and render the terms_of_service template """

    title = 'Terms of Service - ArtsyVisions.com';
    template = 'content/legal/terms_of_service.html'
    context = {
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
        'title': title,
    }
    return render(request, template, context)

##
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##   Views for Quiz Pages
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##

def quiz_about(request):

    """ Load and render the quiz_about page template """

    quiz_info = {}
    quiz_info["quiz_size_abbr"] = ''
    quiz_info["question_count"] = 0
    quiz_info["size_text"] = ''

    quiz_list_data = Questionnaire.get_quiz_list_data()
    template = loader.get_template('content/quiz_about.html')
    context = {
        'quiz_info': quiz_info,
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
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
                    score.set_quiz_results_messages(request)
                    saved_messages = score.save_questionnaire(
                            quiz_form.cleaned_data, quiz_size_slug)
                    for saved_msg in saved_messages:
                        messages.add_message(request, messages.INFO, saved_msg)
                    template = loader.get_template('content/quiz_results.html')
                    score_for_context = score.as_list_of_pairs()
                    return HttpResponse(template.render(
                        { 'score': score_for_context,
                          'quiz_menu_data': quiz_menu_data,},
                        request
                    ))
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

##
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##   Views for Pages for Google
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##

def google203aca4a4dd53796(request):

    """ Load and render the google203aca4a4dd53796 verification template """

    template = loader.get_template('content/google203aca4a4dd53796.html')
    context = {}
    return HttpResponse(template.render(context, request))


def google428ef5aab2bc0870(request):

    """ Load and render the google428ef5aab2bc0870 verification template """

    template = loader.get_template('content/google428ef5aab2bc0870.html')
    context = {}
    return HttpResponse(template.render(context, request))
