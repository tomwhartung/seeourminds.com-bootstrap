
# Installing Django

This directory is a work area for globally installing the current stable version of Django.

## Commands

Here are the commands to run to complete this process:

```
git clone git@github.com:django/django.git
cd django/
git checkout stable/1.10.x
git status   # check status
git branch   # check branch
git log      # commit 8f428c82969d6f1e90f9fe2cbaff346d5d8c711a - dated Sat Oct 15
cd ..
sudo -H pip3 install django
```

To check the installation:

```
python -m django --version                           ## not installed for python2
python -c "import django; print(django.__path__)"    ## not installed for python2
python3 -m django --version                          ## 1.10.2
python3 -c "import django; print(django.__path__)"   ## ['/usr/local/lib/python3.5/dist-packages/django']
```

## For More Context

To see these commands in contxt of this entire process, see:

* https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/ubuntu/general/2-hosting_django-jane.txt and
* https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/ubuntu/specific_hosts/2-hosting_django-barbara.txt

