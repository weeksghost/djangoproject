import datetime
import os
import sys
import urllib
import shutil
import time
from time import mktime

import fish
from fabric.api import cd, env, local, run, sudo
from fabric.context_managers import hide, settings
from fabric.utils import fastprint


UTIL_ROOT = os.path.join(os.path.dirname(__file__), 'utilities')
sys.path.insert(0, UTIL_ROOT)


def fresh(listen='127.0.0.1', port=8000):
    """Executes runserver"""
    local('./manage.py cache_clear')
    local('./manage.py runserver %s:%s' % (listen, port))


def fresh0():
    """Starts up on 0.0.0.0:8000"""
    local('./manage.py runserver 0.0.0.0:8000')


def cc():
    with settings(hide('warnings'), warn_only=True):
        local('cd compass && compass compile && cd ..')


def cs():
    local('./manage.py collectstatic --noinput')
