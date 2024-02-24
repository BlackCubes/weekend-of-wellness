"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

DJANGO_SETTINGS_MODULE = (
    "core.settings.prod" if os.getenv("IN_PRODUCTION") == "1" else "core.settings.dev"
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)


application = get_asgi_application()
