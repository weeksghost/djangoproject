from djangoproject.universal_settings import*

import os

HOME = os.getenv("HOME")

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

ADMINS = (
     ('YOUR NAME', 'YOUR_EMAIL@EXAMPLE.COM'),
)

MANAGERS = ADMINS

ROOT_URLCONF = 'djangoproject.settings.example.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'database.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/tmp/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory that holds static files.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/tmp/static/'

# URL that handles the static files served from STATIC_ROOT.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

STATICFILES_DIRS = (
        HOME + '/djangoproject/static',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'j-39$ty7jpf8fi+oubglzwy6+8pg&ot518qt)1tuqu++nvbj&%'

INSTALLED_APPS += (
    'django_extensions',
    'south',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

TEMPLATE_DIRS = (
        HOME + '/djangoproject/templates',
)

# Celery
BROKER_URL = "amqp://<RABBIT_USER>:<RABBIT_PASSWORD>@localhost:5672//<RABBIT_VHOST>"
CELERY_RESULT_BACKEND = "database"

# choose the setting that matches your database of choice
CELERY_RESULT_DBURI = "mysql://<DB_USER>:<DB_PASSWORD>@localhost/<DB_NAME>"
CELERY_RESULT_DBURI = "postgresql://<DB_USER>:<DB_PASSWORD>@localhost/<DB_NAME>"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
}

import djcelery
djcelery.setup_loader()

