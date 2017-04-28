#!/bin/bash
#
#  createsuperuser.sh: tiny shell script to create a superuser for this app
#
export PYTHONPATH="..:${PYTHONPATH}"
python3 -m manage createsuperuser
