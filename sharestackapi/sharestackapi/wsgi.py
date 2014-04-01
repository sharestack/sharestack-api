"""
WSGI config for sharestackapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os

machine_env = os.environ.get("SHARESTACK_API_DJANGO_SETTINGS_MODULE", None)

if machine_env == "production":
    settings_env = "sharestackapi.settings.production"
elif machine_env == "staging":
    settings_env = "sharestackapi.settings.staging"
elif machine_env == "test":
    settings_env = "sharestackapi.settings.test"
else:
    settings_env = "sharestackapi.settings.local"

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_env)
os.environ["DJANGO_SETTINGS_MODULE"] = settings_env  # Force it!

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
