import django.db.models
from django.db import models

from .profile.user_profile import UserProfile
from .base import Base


class ChatRoom(Base):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(UserProfile)

    def __str__(self) -> str:
        return f'Chat-room "{self.name}" id - {self.pk}'

    def get_members(self) -> django.db.models.QuerySet | list:
        return list(self.members) or self.members

    @classmethod
    def get_cr_count(cls):
        return ChatRoom.objects.count()
