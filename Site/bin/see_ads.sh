#!/bin/bash
#
#  see_ads.sh: run development server but fetch and display ads from google nonetheless
#
## export DJANGO_DEBUG=1
## export RUNNING_LOCALLY=1
export PYTHONPATH="..:${PYTHONPATH}"
python3 -m manage runserver
