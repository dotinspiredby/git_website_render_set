"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import environ
from django.core.wsgi import get_wsgi_application

env = environ.Env()
# reading .env file
environ.Env.read_env()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")

application = get_wsgi_application()

from django.contrib.auth.models import User
users = User.objects.all()
if not users:
    User.objects.create_superuser(username=env("ADMIN"), email=env("ADMIN_EMAIL"),
                                  password=env("ADMIN_PASSWORD"), is_active=True, is_staff=True)
