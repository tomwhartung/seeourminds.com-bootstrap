#!/bin/bash
#
#  run.sh: tiny shell script to run the development server for this app
#
## export DJANGO_DEBUG=1
export USE_AD_PLACEHOLDERS=1
export PYTHONPATH="..:${PYTHONPATH}"
python3 -m manage runserver
