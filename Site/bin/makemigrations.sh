#!/bin/bash
#
#  makemigrations.sh: tiny shell script to run makemigrations for this app
#
export PYTHONPATH="..:${PYTHONPATH}"
python3 -m manage makemigrations
