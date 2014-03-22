import os

from .base import *


SECRET_KEY = 'h6b@%vt1oc-n_z&66uz0uj*_3pt#_%+h9mnpzsrb-&liiv#olj'

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "sharestack",
        "USER": "postgres",
        "PASSWORD":  "",
        "HOST": 127.0.0.1,
        "PORT": 5432,
    }
}
