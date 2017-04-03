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

from .forms import QuizForm
from .models import Quiz


def home(request):

    """ Load and render the Home page template """

    context_home_selected = 'selected-option'      # see seeourminds.css
    template = loader.get_template('content/home.html')
    context = {
        'context_home_selected': context_home_selected,
    }
    return HttpResponse(template.render(context, request))


def galleries(request):

    """ Load and render the Galleries page template """

    context_galleries_selected = 'selected-option'      # see seeourminds.css
    template = loader.get_template('content/galleries.html')
    context = {
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
        'name_of_gallery': name_of_gallery,
        'description_of_gallery': description_of_gallery,
        'image_file_dir': image_file_dir,
        'data_file_path': data_file_path,
        'image_list_with_path': image_list_with_path,
        'row_separator_markup': row_separator_markup,
    }
    return HttpResponse(template.render(context, request))


def quiz(request):

    """ Load and render the Quiz page template """

    if request.method == 'POST':
        quiz_form = QuizForm(request.POST)
        #
        #  Form processing is tbd...
        #  We are not yet doing anything with this data on the server
        #
        if quiz_form.is_valid():
            # name = quiz_form.cleaned_data['name']
            # email = quiz_form.cleaned_data['email']
            # print('form is valid, got name:', name)
            # print('form is valid, got email:', email)
            # redirect to a new URL:
            # print('quiz_form.cleaned_data:', quiz_form.cleaned_data)
            print('views.quiz() - len(quiz_form.cleaned_data):',
                    len(quiz_form.cleaned_data))
            quiz_model = Quiz()
            score = quiz_model.score_quiz(quiz_form.cleaned_data)
            four_letter_type = "Type: " + score.as_four_letter_type()
            # quiz_results_counts = "Counts: " + score.__str__()
            # quiz_results_pcts = "Percentages: " + score.as_percentages()
            # counts_and_pcts = "Score: " + score.as_counts_and_pcts()
            messages.add_message(request, messages.INFO, four_letter_type)
            # messages.add_message(request, messages.INFO, quiz_results_counts)
            # messages.add_message(request, messages.INFO, quiz_results_pcts)
            # messages.add_message(request, messages.INFO, counts_and_pcts)
            # score_list = score.as_list_of_counts_and_pcts()
            # counts_and_pcts_html = '<ul>'
            # for score_pair in score_list:
            #     counts_and_pcts_html += '<li>'
            #     for single_score in score_pair:
            #         counts_and_pcts_html += single_score + '&nbsp;'
            #     counts_and_pcts_html += '</li>'
            # counts_and_pcts_html += '</ul>'
            # messages.add_message(request, messages.INFO, counts_and_pcts_html)
            score_list = score.as_list_of_pcts_and_counts()
            pcts_and_counts_html = '<ul>'
            for score_pair in score_list:
                pcts_and_counts_html += '<li>'
                for single_score in score_pair:
                    pcts_and_counts_html += single_score + '&nbsp;'
                pcts_and_counts_html += '</li>'
            pcts_and_counts_html += '</ul>'
            messages.add_message(request, messages.INFO, pcts_and_counts_html)
            return HttpResponseRedirect('/quiz/results')
    else:
        quiz_form = QuizForm()

    context_quiz_selected = 'class="selected-option"'    # see seeourminds.css
    template = loader.get_template('content/quiz.html')
    context = {
        'context_quiz_selected': context_quiz_selected,
        'quiz_form': quiz_form
    }
    return HttpResponse(template.render(context, request))


def quiz_results(request):
    """ Render the Quiz results template """
    # quiz_results = request.session['quiz_results']
    quiz_results = 'quiz results here'
    return render(request, 'content/quiz_results.html', {'quiz_results': quiz_results})


def google_verification(request):

    """ Load and render the google verification template """

    template = loader.get_template('content/google428ef5aab2bc0870.html')
    context = {}
    return HttpResponse(template.render(context, request))
