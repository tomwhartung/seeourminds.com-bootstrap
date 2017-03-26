#!/bin/bash
#
#  run.sh: tiny shell script to run the development server for this app
#
export PYTHONPATH="..:${PYTHONPATH}"
python3 -m manage runserver
