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
  context_heading = 'New!'
  context_ptags_01 = 'Welcome to the NEW SeeOurMinds.com!  '
  context_ptags_02 = 'Sorry to disappoint you, but we upgraded our server and there is nothing here right now!  '
  context_ptags_03 = 'We are busy learning and playing around with the latest technologies, so check back again soon!  '
  context_leading_ptags = [ context_ptags_01, context_ptags_02, context_ptags_03 ]
  template = loader.get_template('content/index.html')
  context = {
    'context_heading': context_heading,
    'context_leading_ptags': context_leading_ptags,
  }
  return HttpResponse(template.render(context, request))

##
# load and render the template with a context containing
# heading and content specific to the quiz page
#
def quiz(request):
  context_heading = 'The SeeOurMinds.com Quiz'
  context_content = 'Welcome to the quiz page.  There is nothing here right now; please try again later.  '
  template = loader.get_template('content/index.html')
  context = {
    'context_heading': context_heading,
    'context_content': context_content,
  }
  return HttpResponse(template.render(context, request))

