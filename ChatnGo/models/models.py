from collections.abc import Iterable
from typing import Any, List

import django.db.models
from django.db import models
from django.db.models import manager

from .base import Base
from .profile.user_profile import UserProfile


class ChatRoom(Base):
    # ChatRoom model

    name: str = models.CharField(max_length=255)
    members: manager = models.ManyToManyField(UserProfile)

    def __str__(self) -> str:
        return f'Chat-room "{self.name}" id - {self.pk}'

    def get_members(self) -> Any:  # I dont know what im doing
        return list(self.members) or self.members

    @classmethod
    def get_cr_count(cls) -> int:
        return ChatRoom.objects.count()
