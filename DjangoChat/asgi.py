"""
ASGI config for DjangoChat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from ChatnGo.consumers import ChatConsumer
from django.core.asgi import get_asgi_application
from django.urls import re_path, path

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

django_asgi_app = get_asgi_application()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoChat.settings')


application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path(r"ws/", ChatConsumer.as_asgi()),
            ])
        )
    ),
})
