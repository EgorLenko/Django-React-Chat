import django.db.models
from django.db import models

from .profile.user_profile import UserProfile
from .base import Base

from django.db.models import manager


class ChatRoom(Base):
    # ChatRoom model

    name: str = models.CharField(max_length=255)
    members: manager = models.ManyToManyField(UserProfile)

    def __str__(self) -> str:
        return f'Chat-room "{self.name}" id - {self.pk}'

    def get_members(self) -> list | django.db.models.QuerySet:
        return list(self.members) or self.members

    @classmethod
    def get_cr_count(cls) -> int:
        return ChatRoom.objects.count()
