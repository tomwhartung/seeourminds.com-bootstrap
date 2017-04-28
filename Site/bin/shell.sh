#!/bin/bash
#
# shell.sh: tiny shell script to enter the python server
#
# Sample commands:
# >>> from content.database import Answer
# >>> from content.database import Questionnaire
# >>> Answer.objects.all()
# >>> Questionnaire.objects.all()
# >>> ans1 = Answer.objects.filter(id=1)
# >>> ans1                  # <QuerySet [<Answer: 0/1>]>
# >>> ans1 = Answer.objects.get(pk=1)
# >>> ans1                  # <Answer: 0/1>
# >>> quiz1 = Questionnaire.objects.filter(id=1)
# >>> quiz1                 # <QuerySet [<Questionnaire: /john@beatles.net/2XS>]>
# >>> quiz1 = Questionnaire.objects.get(pk=1)
# >>> quiz1                 # <Questionnaire: /john@beatles.net/2XS>
# >>>
# >>>
# >>>
# >>>
# >>>
#
#
export DJANGO_DEBUG=1
export RUNNING_LOCALLY=1
export PYTHONPATH="..:${PYTHONPATH}"
python3 -m manage shell
