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

There is a lot of information there; this README.md file contains only the most essential parts of all of those files.

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

References:

* https://docs.djangoproject.com/en/1.10/topics/install/#install-the-django-code
* https://docs.djangoproject.com/en/1.10/topics/install/#installing-development-version
* https://virtualenv.pypa.io/en/stable/
* https://virtualenvwrapper.readthedocs.io/en/latest/

#### Install pip and virtualenv:

Check to see whether pip3 or virtualenv or both are already installed:

```
which pip3
which virtualenv
```

**NOTE: At this time, I am unsure whether we need these on the production host!!**

If they are not installed, run these commands to install them **(unless on production host?!?)**.

```
sudo apt-get install python3-pip
pip3 install virtualenv
sudo apt install virtualenv   ## Also had to do this, for some strange reason...
```

Create the seeourmindsenv virtual environment, so that it uses python3:

```
virtualenv --python=`which python3` ~/.virtualenvs/seeourmindsenv
```

**NOTE: Because I am unsure whether we need these on the production host, I have created this in my home dir (~/.virtualenvs/...).**

#### Activate the virtual environment and install the current stable version of django in it:

```
. ~/.virtualenvs/seeourmindsenv/bin/activate
```

> "Anything you install through pip from now on will be installed in your new virtualenv, isolated from other environments and system-wide packages. Also, the name of the currently activated virtualenv is displayed on the command line to help you keep track of which one you are using. Go ahead and install the previously cloned copy of Django:"

```
. ~/.virtualenvs/djangodev/bin/activate
cd /var/www/learn/django/github/customizations/always_learning_python/
git clone git://github.com/django/django.git
sudo pip install -e django/
```

#### Verify the virtual environment:

Before entering virtual environment:

```
which python   ## /usr/bin/python
python -V      ## Python 2.7.12
python         ## skipping output before prompt
>>> import django
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named django
>>>
```

After entering virtual environment:

```
. ~/.virtualenvs/djangodev/bin/activate
which python                 ## /home/tomh/.virtualenvs/djangodev/bin/python
python -V                    ## Python 3.5.2
python -m django --version   ## 1.11.dev20160903160000
python                       ## skipping output before prompt
>>> import django
>>> print(django.get_version())
1.11.dev20160903160000
>>> django.__path__
['/var/www/learn/django/github/customizations/always_learning_python/django/django']
>>>
```




