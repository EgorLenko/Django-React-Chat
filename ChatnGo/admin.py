"""Configuration for ChatnGo amdin module."""
from django.contrib import admin

from .models import ChatRoom, Message, UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ChatRoom)
admin.site.register(Message)
