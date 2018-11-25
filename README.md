# seeourminds.com-bootstrap

This obsolete repo contains OLD code for seeourminds.com .

**Please use the new code which uses Material Design Bootstrap and has updated and new content in the current seeourminds.com repo.**

Reinventing seeourminds.com from scratch, in python/django.

## Overview of This Site

After reading a lot about marketing and the new Google Analytics, etc., I've learned how to define this site's purpose.  Cool!

### Combo site

As learned in the Google Analytics (GA) "Getting Started" class, we can define this site as having two purposes:

* Content site - show ads
* Lead generation site - gather email addresses for occasional emails containing newly drawn personalities

We use GA to learn which one or both of these purposes is working.
If it turns out that we are better off having only one purpose per site, we may make modifications accordingly.

#### Content site

As a content site, this site has the following purposes:

* Drive traffic to groja.com our parallel lead generation and e-commerce site
* Show Google AdSense ads

To begin with, this is the primary purpose.

#### Lead-generation site

As a lead-generation site, this site has the following purposes:

* Drive traffic to groja.com our parallel lead generation and e-commerce site
* Gather email addresses for an occasional emails containing newly drawn personalities

To begin with, this is a secondary purpose.

### Technical

Right now the site uses django to deliver minimal html5boilerplate (initializr) content.

**Let's keep it as simple as possible!**

## New Version

I've decided to move the gallery from groja.com to here.

### Gallery Specifics

From the README.md file for groja.com:

* Galleries: `galleries`
  * Friends: `galleries/gallery.html?gallery=friends`
  * Generics: `galleries/gallery.html?gallery=generics`
  * TV Shows: `galleries/gallery.html?gallery=tvshows`
  * Politicians: `galleries/gallery.html?gallery=politicians`

### Other possible menu options:

Thoughts while contemplating what the other menu options should be:

* Quiz (keep)
* All - allow sorting, searching, and filtering all of the images in all of the galleries

Links to groja.com:

* Last link in menu: "Your Portrait" - to groja.com/yourportrait
* In addition, we should also have a link in aside area in one or more pages: to groja.com/hom

Use GA to see which one is working for us, and maybe switch them in the future.

## Setup Notes

Following is some more background, if you're interested.

### Previous experimental efforts

The initial version is essentially what we came up with in the `2-seeourminds-prototype` directory of the `always_learning_python` repo.

The following README.md files contain a lot of details concerning how I have come up with this process:

* https://github.com/tomwhartung/always_learning_python/blob/master/README.md
* https://github.com/tomwhartung/always_learning_python/blob/master/0-hello_world/README.md
* https://github.com/tomwhartung/always_learning_python/blob/master/0-hello_world/startproject/README.md - esp. the say_hi_tomh version
* https://github.com/tomwhartung/always_learning_python/tree/master/2-seeourminds-prototype

There is a lot of information there; this README.md file contains only the most essential parts of all of those files.

### The best "hello world" of the bunch

Having run through several versions of the hello-world and other getting-started-type tutorials, it's obvious this one is the best:

* https://docs.djangoproject.com/en/1.10/intro/tutorial01/

It is not surprising, but good to know.

## Process Overview

This process starts at the very beginning; following is an overview of the steps

1. Download (git clone) the current version of django and set up a virtual environment to use it
2. Use the django-admin command to run startproject and use the development server to test that everything is working so far
3. Use the django-admin command to run startapp
4. Edit important files to get a hello-world-type view working
5. Add in the html5boilerplate (initializr-responsive) code

## Step 1. Setup virtual environment, git clone django, and install it in the virtual env

At this time it seems it would be silly to check in the django source (as we have come to do for the LAMP CMSes), because it's in git.

However, for stability's sake, we want to have an up-to-date stable version it in this directory tree to help with deployment.

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

The command to activate our virtual environment is:

```
. ~/.virtualenvs/seeourmindsenv/bin/activate
```

> "Anything you install through pip from now on will be installed in your new virtualenv, isolated from other environments and system-wide packages. Also, the name of the currently activated virtualenv is displayed on the command line to help you keep track of which one you are using. Go ahead and install the previously cloned copy of Django:"

**Rather than rely on our memory or hope that we see this part of this README.md file, we create a small shell script to run this:**

```
cd /var/www/seeourminds.com/htdocs/seeourminds.com
mkdir virtualenvs
echo  '. ~/.virtualenvs/seeourmindsenv/bin/activate' > virtualenvs/seeourmindsenv.sh
chmod 755 virtualenvs/seeourmindsenv.sh
```

Then we enter the environment, clone django, checkout the stable version of it, and use pip to install it.

**NOTE: Ensure that "django" is in our .gitignore, we do NOT want to check that it!**

```
cd /var/www/seeourminds.com/htdocs/seeourminds.com
. virtualenvs/seeourmindsenv.sh
mkdir djangostable
cd djangostable/
git clone git://github.com/django/django.git
cd django
git checkout stable/1.10.x
git branch    ## verify we are on the stable branch
cd ..
pip install -e django/
```

I am 99% sure that once we install it in the virtual environment, we no longer need the copy of django in this directory:

* /var/www/seeourminds.com/htdocs/seeourminds.com/djangostable/django - no longer needed?

It absolutely should not hurt anything to have it there, though!

(Wow I forgot how complicated all this is, and am glad I made copious notes of what I did last time!)

#### Verify the virtual environment has the correct version of django installed in it:

In a **new** terminal window, before entering virtual environment, our PATH should be "pointing to" the old version:

```
which python   ## /usr/bin/python
python -V      ## Python 2.7.12
```

After entering virtual environment, our PATH **should** be "pointing to" the new version:

```
cd /var/www/seeourminds.com/htdocs/seeourminds.com
. virtualenvs/seeourmindsenv.sh
which python                 ## /home/tomh/.virtualenvs/seeourmindsenv/bin/python
python -V                    ## Python 3.5.2
python -m django --version   ## 1.10.3.dev20161004180341
python                       ## skipping output before prompt
>>> import django
>>> print(django.get_version())
1.10.3.dev20161004180341
>>> django.__path__
['/var/www/seeourminds.com/htdocs/seeourminds.com/djangostable/django/django']
>>>
```

If the verification works as expected, commit our one-liner shell script virtualenvs/seeourmindsenv.sh .

```
git add virtualenvs/seeourmindsenv.sh
git commit 'Adding a small shell script in virtualenvs/ to make it easy to remember which virtualenv want to use for this site.'
```

## Step 2. Use the django-admin command to run startproject

Having run through this process several times by now, we can easily run through the required commands fairly quickly.

For details, see:

* https://github.com/tomwhartung/always_learning_python/blob/master/2-seeourminds-prototype/README.md

Run `django-admin startproject` to start the project:

```
cd /var/www/seeourminds.com/htdocs/seeourminds.com
. virtualenvs/seeourmindsenv.sh
django-admin startproject Site
```

Now use the development server to test that everything is working so far:

```
cd /var/www/seeourminds.com/htdocs/seeourminds.com
. virtualenvs/seeourmindsenv.sh
cd Site/
python manage.py runserver      ## Use Ctrl-C to stop the server
```

Ignore the errors about database migrations, and access the following URL in a browser:

* http://localhost:8000

You should see an "It worked!" message on a pale blue background.

## Step 3. Use the django-admin command to run startapp

There's no reason to run the `cd` and `.` commands if your terminal window is already in the correct directory and environment.

```
cd /var/www/seeourminds.com/htdocs/seeourminds.com
. virtualenvs/seeourmindsenv.sh
cd Site/
django-admin startapp content
```

Go ahead and commit the un-edited versions of these files, so if we mess soemthing up, we can always return to them.

```
git add .
git commit -m 'Adding the default, generated version of files created running django-admin startproject and startapp.'
```

## Step 4. Edit important files to get a hello-world-type view working

Make the following edits:

1. Add routes to content/urls.py, so that visitors are "taken to" views.index
2. Edit content/views.py
3. Edit Site/urls.py, so that we use the routes in content/urls.py
4. Edit Site/settings.py , adding "content" as one of the "INSTALLED_APPS" and commenting out the db stuff for now

## Step 5. Add in the html5boilerplate (initializr-responsive) code

This step uses files edited earlier in the 2-seeourminds-prototype directory of the always_learning_python repo.

1. Copy the edited html5boilerplate index.html into content/templates/content and edit as appropriate
2. Copy the supporting html5boilerplate css and js into the proper directories (static/content/css and static/content/js)
3. Update views.py to use the template instead of just returning the "hello world" text

## Step 6. Get site to run through apache instead of just the development server.

Reference: https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/

For the detailed steps needed to get that going, see :

* https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/ubuntu/general/2-hosting_django-jane.txt and
* https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/ubuntu/specific_hosts/2-hosting_django-barbara.txt

## Conclusion

Along with all the experimentation/playing-around/work done in the various always_learning_python projects, this has been quite the learning experience!

