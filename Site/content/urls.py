#
# urls.py for our content app
#
from django.conf.urls import *

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home$', views.home, name='home'),
    url(r'^galleries$', views.galleries, name='galleries'),
    url(r'^gallery/(?P<gallery_name>\w+)/$', views.gallery, name='gallery'),
    url(r'^quiz$', views.quiz, name='quiz'),
]
