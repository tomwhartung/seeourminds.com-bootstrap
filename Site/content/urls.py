""" urls.py for our content app

Purpose: define the urls for this app
Author: Tom W. Hartung
Date: Winter, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none)
"""

from django.conf.urls import *

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home$', views.home, name='home'),
    url(r'^galleries$', views.galleries, name='galleries'),
    url(r'^gallery/(?P<gallery_name>\w+)/$', views.gallery, name='gallery'),
    url(r'^image/$', views.image, name='image'),
    url(r'^image/(?P<image_path>\w+)/$', views.image, name='image'),
    url(r'^quiz$', views.quiz, name='quiz'),
    url(r'^quiz/results$', views.quiz_results, name='quiz_results'),
    url(r'^google428ef5aab2bc0870.html$',
        views.google_verification, name='google_verification'),
]
