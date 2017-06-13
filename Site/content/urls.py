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
    url(r'^galleries/(?P<galleries_list_name>\S+)/$', views.galleries, name='galleries'),
    url(r'^gallery/(?P<gallery_file_name>\S+)/$', views.gallery, name='gallery'),
    url(r'^image/$', views.image, name='image'),
    url(r'^image/(?P<image_id>\w+)/$', views.image, name='image'),
    url(r'^image/(?P<gallery_file_name>\S+)/(?P<image_id>\w+)/$', views.image, name='image'),
    url(r'^quiz$', views.quiz_about, name='quiz_about'),
    url(r'^quiz/(?P<quiz_size_slug>[\w-]+)/$', views.quiz_form, name='quiz_form'),
    url(r'^google428ef5aab2bc0870.html$',
        views.google_verification, name='google_verification'),
]
