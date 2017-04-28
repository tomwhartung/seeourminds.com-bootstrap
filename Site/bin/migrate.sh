#!/bin/bash
#
#  migrate.sh: tiny shell script to run migrate for this app
#
export PYTHONPATH="..:${PYTHONPATH}"
python3 -m manage migrate
