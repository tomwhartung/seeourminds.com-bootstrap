#!/bin/bash
#
#  run.sh: tiny shell script to run the development server for this app
#
export DJANGO_DEBUG=1
export RUNNING_LOCALLY=1
export PYTHONPATH="..:${PYTHONPATH}"
python3 -m manage runserver
