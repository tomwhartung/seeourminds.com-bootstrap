#!/bin/bash
#
#  collectstatic.sh: tiny shell script to collect the static files into ../static/*
#
export PYTHONPATH="..:${PYTHONPATH}"
python3 -m manage collectstatic --noinput --clear
touch ../static/.this_dir_intentionally_left_empty
