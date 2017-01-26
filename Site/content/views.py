from django.shortcuts import render

# Create your views here.

import textwrap

from django.http import HttpResponse
from django.views.generic.base import View
from django.template import loader

##
# load and render the template with a context containing
# heading and content specific to the home page
#
def home(request):
  context_home_selected = 'selected'
  template = loader.get_template('content/home.html')
  context = {
    'context_home_selected': context_home_selected,
  }
  return HttpResponse(template.render(context, request))

##
# load and render the template with a context containing
# heading and content specific to the quiz page
#
def quiz(request):
  context_quiz_selected = 'selected'
  context_heading = 'The SeeOurMinds.com Quiz'
  context_leading_ptags = [
    'Welcome to the quiz page.',
    'We are working on this, so please try again later.',
  ]
  template = loader.get_template('content/quiz.html')
  context = {
    'context_quiz_selected': context_quiz_selected,
    'context_heading': context_heading,
    'context_leading_ptags': context_leading_ptags,
  }
  return HttpResponse(template.render(context, request))
