import os

from .base import *


SECRET_KEY = os.environ.get('SHARESTACK_API_DJANGO_SECRET_KEY')

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get('SHARESTACK_DB_NAME'),
        "USER": os.environ.get('SHARESTACK_DB_USER'),
        "PASSWORD":  os.environ.get('SHARESTACK_DB_PASSWORD'),
        "HOST": os.environ.get('SHARESTACK_DB_HOST'),
        "PORT": os.environ.get('SHARESTACK_DB_PORT'),
    }
}
