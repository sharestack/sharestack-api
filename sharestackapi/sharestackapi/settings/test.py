from .base import *


DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = 'htyu@%vt15c-n_z&6*uz026j*_3p2#_%+h9mnpzsrb-&liiv#K0'

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
