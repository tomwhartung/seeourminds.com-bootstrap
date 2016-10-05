from django.shortcuts import render

# Create your views here.

import textwrap

from django.http import HttpResponse
from django.views.generic.base import View
from django.template import loader

##
## From part 1 of the polls tutorial; the simplest view:
## Reference: "Write your first view" section
##    https://docs.djangoproject.com/en/1.10/intro/tutorial01/
## Runs when we access:
##    http://127.0.0.1:8000/index
##
def index(request):
    return HttpResponse("Hello from the index function in content/views.py .")

def index_future(request):
    context_var = 'arbitrary greeting text in a context variable'
    template = loader.get_template('content/index.html')
    context = {
        'context_var': context_var,
    }
    return HttpResponse(template.render(context, request))

