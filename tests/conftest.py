# -*- coding: utf-8 -*-
import os
from django.conf import settings


DIRNAME=os.path.dirname(__file__)


def pytest_configure():
    settings.configure(
        DEBUG=True,
        TESTING=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': 'dknorway-testing.db',  # Or path to database file if using sqlite3.
                # The following settings are not used with sqlite3:
                'USER': '',
                'PASSWORD': '',
                'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
                'PORT': '',  # Set to empty string for default.
            }
        },
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.admin',
            'dknorway',
            #'myapp.tests',
        )
    )
