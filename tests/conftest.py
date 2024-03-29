# -*- coding: utf-8 -*-
import os

import django

DIRNAME = os.path.dirname(__file__)


def pytest_configure():
    from django.conf import settings
    settings.configure(
        DEBUG=True,
        TESTING=True,
        SECRET_KEY='test',
        CACHES={
            'default': {
                'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
                'LOCATION': os.path.join(DIRNAME, 'cache'),
                'TIMEOUT': 60 * 60,
                'OPTIONS': {
                    'MAX_ENTRIES': 5000
                }
            }
        },
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': os.path.join(DIRNAME, 'dknorway-testing.db'),  # Or path to database file if using sqlite3.
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
            'django.contrib.admin',
            'dknorway',
            #'myapp.tests',
        )
    )
    django.setup()
