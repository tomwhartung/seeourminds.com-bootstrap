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
    url(r'^galleries$', views.galleries_list, name='galleries_list'),
    url(r'^galleries/$', views.galleries_list, name='galleries_list'),
    url(r'^galleries/(?P<galleries_list_name>\S+)/$',
        views.galleries_list,
        name='galleries_list'),
    url(r'^gallery/(?P<gallery_file_name>\S+)/$',
        views.gallery,
        name='gallery'),
    url(r'^image/$', views.image, name='image'),
    url(r'^image/(?P<image_id>\w+)/$', views.image, name='image'),
    url(r'^image/(?P<gallery_file_name>\S+)/(?P<image_id>\w+)$',
        views.image,
        name='image'),
    url(r'^image/(?P<gallery_file_name>\S+)/(?P<image_id>\w+)/$',
        views.image,
        name='image'),
    url(r'^image/$', views.image, name='image'),
    url(r'^legal$', views.legal, name='legal'),
    url(r'^legal/terms_of_service',
        views.terms_of_service,
        name='terms_of_service'),
    url(r'^legal/privacy_policy',
        views.privacy_policy,
        name='privacy_policy'),
    url(r'^legal/questionnaire_disclaimer',
        views.questionnaire_disclaimer,
        name='questionnaire_disclaimer'),
    url(r'^legal/affiliate_marketing_disclosure',
        views.affiliate_marketing_disclosure,
        name='affiliate_marketing_disclosure'),
    url(r'^quiz$', views.quiz_about, name='quiz_about'),
    url(r'^quiz/$', views.quiz_about, name='quiz_about'),
    url(r'^quiz/(?P<quiz_size_slug>[\w-]+)$',
        views.quiz_form,
        name='quiz_form'),
    url(r'^quiz/(?P<quiz_size_slug>[\w-]+)/$',
        views.quiz_form,
        name='quiz_form'),
    url(r'^google203aca4a4dd53796.html$',
        views.google203aca4a4dd53796,
        name='google203aca4a4dd53796'),
    url(r'^google428ef5aab2bc0870.html$',
        views.google428ef5aab2bc0870,
        name='google428ef5aab2bc0870'),
    url(r'^404/(?P<unknown_page>[\w\W]+)$',
        views.not_found,
        name='not_found'),
    url(r'^(?P<unknown_page>[\w\W]+)/$',
        views.process_shortcut,
        name='process_shortcut'),
    url(r'^(?P<unknown_page>[\w\W]+)$',
        views.process_shortcut,
        name='process_shortcut'),
]
