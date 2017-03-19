from django.shortcuts import render

# Create your views here.

import textwrap

from django.http import HttpResponse
from django.views.generic.base import View
from django.template import loader

##
# load and render the Home page template
#
def home(request):
  context_home_selected = 'selected'
  template = loader.get_template('content/home.html')
  context = {
    'context_home_selected': context_home_selected,
  }
  return HttpResponse(template.render(context, request))

##
# load and render the Galleries page template
#
def galleries(request):
  context_galleries_selected = 'selected'
  template = loader.get_template('content/galleries.html')
  context = {
    'context_galleries_selected': context_galleries_selected,
  }
  return HttpResponse(template.render(context, request))

##
# load and render the template for a single Gallery page
#
def gallery(request, gallery_name='all'):
  import json
  import os
  context_gallery_name = gallery_name
  site_content_dir = os.path.abspath(os.path.dirname(__file__))
  data_file_name = gallery_name + '.json'
  data_file_path = site_content_dir + '/static/content/json/galleries/' + data_file_name
  gallery_json_file = open( data_file_path )
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
    image_list_with_path.append( img_to_add )
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

##
#  load and render the Quiz page template
#
from .forms import QuizForm
def quiz(request):
   context_quiz_selected = 'selected'
   template = loader.get_template('content/quiz.html')
   context = {
     'context_quiz_selected': context_quiz_selected,
   }
   ## return HttpResponse(template.render(context, request))
   if request.method == 'POST':
      quiz_form = QuizForm( request.POST )
      #
      #  Form processing is tbd (using javascript to score the quiz in the browser)
      #  We are not yet doing anything with this data on the server
      #
      if quiz_form.is_valid():
         name = quiz_form.cleaned_data['name']
         email = quiz_form.cleaned_data['email']
         print( 'form is valid, got name:', name )
         print( 'form is valid, got email:', email )
         # redirect to a new URL:
         return HttpResponseRedirect('/quiz/')
   else:
      quiz_form = QuizForm()

   return render(request, 'content/quiz.html', {'quiz_form': quiz_form})


##
# load and render the google verification template
#
def google_verification(request):
  template = loader.get_template('content/google428ef5aab2bc0870.html')
  context = { }
  return HttpResponse(template.render(context, request))
