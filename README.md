# seeourminds.com

Reinventing seeourminds.com from scratch, in python/django.

## Overview - This Site

Right now the site uses django to deliver minimal html5boilerplate (initializr) content.

### Previous experimental efforts

The initial version is essentially what we came up with in the `2-seeourminds-prototype` directory of the `always_learning_python` repo.

The following README.md files contain a lot of details concerning how I have come up with this process:

* https://github.com/tomwhartung/always_learning_python/blob/master/README.md
* https://github.com/tomwhartung/always_learning_python/blob/master/0-hello_world/README.md
* https://github.com/tomwhartung/always_learning_python/blob/master/0-hello_world/startproject/README.md - esp. the say_hi_tomh version
* https://github.com/tomwhartung/always_learning_python/tree/master/2-seeourminds-prototype

There is a lot of information there; this README.md file contains only the most essential parts of it.

### The best "hello world" of the bunch

Having gone through several versions of the django hello-world and other getting-started-type projects, it's obvious this one is the best:

* https://docs.djangoproject.com/en/1.10/intro/tutorial01/

## Process Overview

This process starts at the very beginning; following is an overview of the steps

1. Download (git clone) the current version of django and set up a virtual environment to use it
2. Use the django-admin command to run startproject and use the development server to test that everything is working so far
3. Use the django-admin command to run startapp
4. Edit important files to get a hello-world-type view working
5. Add in the html5boilerplate (initializr-responsive) code

## Process Details

At this time it seems it would be silly to check in the django source (as we have come to do for the LAMP CMSes), because it's in git.

However, for stability's sake, we want to have an up-to-date stable version it in this directory tree to help with deployment.

### Git clone django and setup virtual environment



