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
  context_leading_ptags = [
    'Welcome to the NEW SeeOurMinds.com!',
    'We recently upgraded our server.  The old, clunky joomla site is gone, and this is now a (minimal) django site!',
    'So there is not much here right now; currently there is not even a database.  Move along hackers, nothing to see here!',
    'We are busy learning about and playing around with technologies such as the following:',
  ]
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

