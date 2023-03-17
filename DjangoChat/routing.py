from asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

import ChatnGo.routing
# from ChatnGo.consumers import ChatConsumer
# from django.urls import path

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
