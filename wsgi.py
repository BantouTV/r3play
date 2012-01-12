#!/usr/local/bin/python
import os, sys
sys.path.append('/home/ec2-user/')
sys.path.append('/home/ec2-user/r3play/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'r3play.settings'  # this is your settings.py file
os.environ['PYTHON_EGG_CACHE'] = '/tmp'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()