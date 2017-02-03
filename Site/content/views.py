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
  from django.contrib.staticfiles.templatetags.staticfiles import static
  context_gallery_name = gallery_name
  data_file_name = 'content/json/galleries/' + gallery_name + '.json'
  data_file_path = static( data_file_name )
  gallery_json_data = open( data_file_path )
  gallery_json_deserialized = json.load( gallery_json_data )
  gallery_json_type = type( gallery_json_deserialized )
  gallery_json_len = len( gallery_json_deserialized )
  template = loader.get_template('content/gallery.html')
  context = {
    'context_gallery_name': context_gallery_name,
    'gallery_json_type': gallery_json_type,
    'gallery_json_len': gallery_json_len,
    'data_file_path': data_file_path,
    'gallery_json_deserialized': gallery_json_deserialized,
  }
  return HttpResponse(template.render(context, request))

##
# load and render the Quiz page template
#
def quiz(request):
  context_quiz_selected = 'selected'
  template = loader.get_template('content/quiz.html')
  context = {
    'context_quiz_selected': context_quiz_selected,
  }
  return HttpResponse(template.render(context, request))
