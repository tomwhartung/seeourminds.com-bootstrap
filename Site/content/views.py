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
  content_s1 = 'Welcome to the NEW SeeOurMinds.com!  '
  content_s2 = 'Sorry to disappoint you, but we upgraded our server and there is nothing here right now!  '
  content_s3 = 'We are busy learning and playing around with the latest technologies, so check back again soon!  '
  context_content = content_s1 + content_s2 + content_s3
  template = loader.get_template('content/index.html')
  context = {
    'context_heading': context_heading,
    'context_content': context_content,
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

