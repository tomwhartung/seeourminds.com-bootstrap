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
  context_trailing_ptags = [
    'New trailing ptags!'
  ]
  template = loader.get_template('content/home.html')
  context = {
    'context_trailing_ptags': context_trailing_ptags,
  }
  return HttpResponse(template.render(context, request))

##
# load and render the template with a context containing
# heading and content specific to the quiz page
#
def quiz(request):
  context_heading = 'The SeeOurMinds.com Quiz'
  context_leading_ptags = [
    'Welcome to the quiz page.',
    'There is nothing here right now; please try again later.',
  ]
  template = loader.get_template('content/index.html')
  context = {
    'context_heading': context_heading,
    'context_leading_ptags': context_leading_ptags,
  }
  return HttpResponse(template.render(context, request))
