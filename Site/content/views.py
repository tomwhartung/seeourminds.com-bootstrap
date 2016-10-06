from django.shortcuts import render

# Create your views here.

import textwrap

from django.http import HttpResponse
from django.views.generic.base import View
from django.template import loader

##
# load and render the template with a context containing a single variable
#
def index(request):
  context_var = 'arbitrary greeting text in a context variable'
  template = loader.get_template('content/index.html')
  context = {
    'context_var': context_var,
  }
  return HttpResponse(template.render(context, request))

