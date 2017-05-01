#!/bin/bash
#
# run.sh: tiny shell script to run the development server for this app
#
# Setting RUNNING_LOCALLY does the following:
# - causes app to display grey boxes instead of ads
# - enables the tiny sized quiz (containing 4 questions for testing) option
#
export DJANGO_DEBUG=1
export RUNNING_LOCALLY=1
export PYTHONPATH="..:${PYTHONPATH}"
python3 -m manage runserver
