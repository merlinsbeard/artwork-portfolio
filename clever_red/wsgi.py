"""
WSGI config for clever_red project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# Where the setting for prod is located
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clever_red.settings.prod")

application = get_wsgi_application()
