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
  context_ptags_01 = 'Welcome to the NEW SeeOurMinds.com!'
  context_ptags_02 = 'Sorry to disappoint you, but we upgraded our server and there is nothing here right now!'
  context_ptags_03 = 'We are busy learning and playing around with new technologies such as the following:'
  context_leading_ptags = [ context_ptags_01, context_ptags_02, context_ptags_03 ]
  context_main_litags = [
    'LAMP CMSes', 'AWD, RESS, and Device Detection', 'https', 'REST',
    'ES6', 'React', 'PWAs', 'python', 'node', 'django', 'PostgreSql',
    'and many more...'
  ]
  context_trailing_ptags = [
    'We are also delving deeply into some face-to-face user experience (UX) and use case studies.  Never a dull moment!',
    'So, check back in a bit and hopefully we will have something new for you!',
  ]
  template = loader.get_template('content/index.html')
  context = {
    'context_heading': context_heading,
    'context_leading_ptags': context_leading_ptags,
    'context_main_litags': context_main_litags,
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

