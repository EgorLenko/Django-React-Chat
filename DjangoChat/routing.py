import ChatnGo.routing
from ChatnGo.consumers import ChatConsumer
from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

from asgi import get_asgi_application


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                # path("chat/<str:room_name>/", ChatConsumer.as_asgi()),
                ChatnGo.routing.websocket_urlpatterns
            ])
        )
    ),
})
