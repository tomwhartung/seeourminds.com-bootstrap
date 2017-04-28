""" views.py for our content app

Purpose: define the views for this app
Author: Tom W. Hartung
Date: Winter, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none)
"""

from django.shortcuts import render
import textwrap

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.base import View

from .adsense import adsense_ads
from .database import Questionnaire
from .forms import QuestionnaireForm
from .models import Score


def home(request):

    """ Load and render the Home page template """

    context_home_selected = 'class="disabled"'      # see seeourminds.css
    template = loader.get_template('content/home.html')
    context = {
        'adsense_ads': adsense_ads,
        'context_home_selected': context_home_selected,
    }
    return HttpResponse(template.render(context, request))


def galleries(request):

    """ Load and render the Galleries page template """

    context_galleries_selected = 'class="disabled"'      # see seeourminds.css
    template = loader.get_template('content/galleries.html')
    context = {
        'adsense_ads': adsense_ads,
        'context_galleries_selected': context_galleries_selected,
    }
    return HttpResponse(template.render(context, request))


def gallery(request, gallery_name='all'):

    """ Load and render the template for a single Gallery page """

    import json
    import os
    context_gallery_name = gallery_name
    site_content_dir = os.path.abspath(os.path.dirname(__file__))
    data_file_name = gallery_name + '.json'
    data_file_dir = site_content_dir + '/static/content/json/galleries/'
    data_file_path = data_file_dir + data_file_name
    gallery_json_file = open(data_file_path)
    gallery_json_string = gallery_json_file.read()
    gallery_json_file.close()
    gallery_dictionary = json.loads(gallery_json_string)
    name_of_gallery = gallery_dictionary['name_of_gallery']
    description_of_gallery = gallery_dictionary['description_of_gallery']
    image_file_dir = 'content/images/galleries/' + gallery_name + '/'
    image_list = gallery_dictionary['image_list']
    image_list_with_path = []
    for img in image_list:
        img_to_add = img
        img_to_add['image_file_path'] = image_file_dir + img['image_file_name']
        image_list_with_path.append(img_to_add)
    row_separator_markup = "\n</div><!-- .row -->\n<div class='row'>\n"
    template = loader.get_template('content/gallery.html')
    context = {
        'adsense_ads': adsense_ads,
        'name_of_gallery': name_of_gallery,
        'description_of_gallery': description_of_gallery,
        'image_file_dir': image_file_dir,
        'data_file_path': data_file_path,
        'image_list_with_path': image_list_with_path,
        'row_separator_markup': row_separator_markup,
    }
    return HttpResponse(template.render(context, request))


def quiz(request, quiz_size_slug=None):

    """ Load and render the Quiz page template """

    quiz_form = None
    if request.method == 'POST':
        print('views.quiz() - request.POST:', request.POST)
        try:
            email = request.POST["email"]
            load_answers = request.POST["load-answers"]
        except:
            email = ''
            load_answers = ''
        if load_answers == '':
            quiz_form = QuestionnaireForm(
                    quiz_size_slug=quiz_size_slug, data=request.POST)
            if quiz_form.is_valid():
                print('views.quiz() - quiz_form is_valid')
                score = Score()
                score.score_quiz(quiz_size_slug, quiz_form.cleaned_data)
                if score.is_complete():
                    print('views.quiz() - score is_complete')
                    score.save_questionnaire(quiz_form.cleaned_data, quiz_size_slug)
                    score.set_quiz_results_messages(request)
                    return HttpResponseRedirect('/quiz/results')
                else:
                    print('views.quiz() - score is NOT complete')
                    score.set_incomplete_message(request)
        else:
            if email == '':
                need_email_msg = 'ERROR: email is required to load the answers'
                print('views.quiz() -', need_email_msg)
                messages.add_message(request, messages.ERROR, need_email_msg)
            else:
                questionnaire = Questionnaire()
                new_request_post = questionnaire.add_answers(email, request)
                # print('views.quiz() - new_request_post:', new_request_post)
                quiz_form = QuestionnaireForm(
                        quiz_size_slug=quiz_size_slug, data=new_request_post)

    quiz_size_slugs = Questionnaire.get_quiz_size_slugs_list()
    quiz_info = {}
    quiz_info["quiz_size_slug"] = quiz_size_slug
    quiz_slug_text_counts = []
    #
    # If there's no quiz_size_slug, display the quiz landing page,
    # I.e., list the sizes and allows the visitor to select the one they want
    #
    if quiz_size_slug == None:
        quiz_form = None
        quiz_info["size_abbreviation"] = ''
        quiz_info["question_count"] = 0
        quiz_info["size_text"] = ''
        for quiz_size_slug in quiz_size_slugs:
            size_text = Questionnaire.get_quiz_size_text_for_slug(quiz_size_slug)
            question_count = Questionnaire.get_question_count_for_slug(quiz_size_slug)
            print('view.quiz - quiz_size_slug/size_text/question_count:',
                quiz_size_slug + '/' + size_text + '/' + str(question_count))
            size_text_and_count = [quiz_size_slug, size_text, question_count]
            quiz_slug_text_counts.append(size_text_and_count)
    else:
        if quiz_form == None:
            quiz_form = QuestionnaireForm(quiz_size_slug=quiz_size_slug)
        quiz_info["size_abbreviation"] = \
            Questionnaire.get_quiz_size_abbreviation_for_slug(quiz_size_slug)
        quiz_info["question_count"] = \
            Questionnaire.get_question_count_for_slug(quiz_size_slug)
        quiz_info["size_text"] = \
            Questionnaire.get_quiz_size_text_for_slug(quiz_size_slug)

    template = loader.get_template('content/quiz.html')
    context = {
        'adsense_ads': adsense_ads,
        'quiz_form': quiz_form,
        'quiz_info': quiz_info,
        'quiz_slug_text_counts': quiz_slug_text_counts,
    }
    return HttpResponse(template.render(context, request))


def quiz_results(request):
    """ Render the Quiz results template """
    # quiz_results = request.session['quiz_results']
    quiz_results = 'quiz results here'
    return render(request, 'content/quiz_results.html', {'quiz_results': quiz_results})


def image(request, image_id=0):

    """ Render the single image template """

    try:
        image_id_int = int(image_id)
    except:
        print('views.image: non-numeric "image_id" from url: ' + image_id)
        image_id_int = 0

    image = {}
    image["id"] = image_id_int

    if image_id_int == 0:
        image["name"] = 'Tom H., Creator of SeeOurMinds.com and Groja.com'
        image["path"] = 'content/images/header/infp-tomh_1987-515x515.gif'
        image["description"] = 'The image contains mostly blue and red, ' \
           'indicating I am idealistic and passionate.  ' \
           'There is also plenty of green and yellow, however, indicating ' \
           'I can be logical and down-to-earth when the situation calls ' \
           'for it.' \
           'This is just the sort of person who can both conceive of ' \
           'this idea and follow through and learn the details needed to ' \
           'implement it.'
    else:
        image["name"] = 'image_id_int from url: ' + str(image_id_int)
        image["path"] = 'content/images/header/infp-tomh_1987-515x515.gif'
        image["description"] = 'description goes here'

    return render(request, 'content/image.html',
         {'adsense_ads': adsense_ads,
          'image': image,
         })


def google_verification(request):

    """ Load and render the google verification template """

    template = loader.get_template('content/google428ef5aab2bc0870.html')
    context = {}
    return HttpResponse(template.render(context, request))
