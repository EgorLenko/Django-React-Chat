"""Default directory for app configuration class"""
from django.apps import AppConfig


class ChatngoConfig(AppConfig):
    """ChatnGo default configuration"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "ChatnGo"
