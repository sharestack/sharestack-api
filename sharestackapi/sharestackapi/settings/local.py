import os

from .base import *


DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = 'c3b@%tt!oc-n_=&6aiz0uz*_3pt#_%+h9mn0zsrb-&liiv#klj'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "sharestack",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
INTERNAL_IPS = (
    "10.0.2.2",  # Vagrant use (Virtual box default gateway)
    "127.0.0.1",
)

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    "debug_toolbar.middleware.DebugToolbarMiddleware",
)
