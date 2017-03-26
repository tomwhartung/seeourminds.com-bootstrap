""" Define our apps

Purpose: define the content app
Note: I don't think this file is currently being used.
Author: Tom W. Hartung
Date: Winter, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none)
"""

from django.apps import AppConfig


class ContentConfig(AppConfig):
    """ Keeping it simple for now, we have just the content app """
    name = 'content'
