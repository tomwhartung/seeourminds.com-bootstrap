#
# urls.py for our content app
#
from django.conf.urls import *

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
]

