from pymongo import MongoClient
from django.conf import settings
# from djongo import models
from django.db import models
from .base import Base
from .models import UserProfile, ChatRoom

from typing import Any


def get_mongodb_handler(msg_host=settings.MSG_DB['HOST'],
                        msg_port=int(settings.MSG_DB['PORT']),
                        msg_username=settings.MSG_DB['USERNAME'],
                        msg_password=settings.MSG_DB['PASSWORD']):
    # Creating Mongo Client and connecting to MongoDB (currently not-used)

    client = MongoClient(host=msg_host, port=msg_port, username=msg_username, password=msg_password)
    db = client[settings.MSG_DB['NAME']]

    return db, client


class Message(Base):
    # models for storing messages in SQL db
    # TODO 4: change data store type from SQL to NoSQL (MongoDB)

    # Params:
    # content(str[1000]) - message content (the message itself);
    # msg_id(str) - Stores an auto-generated key containing the sender, chat room, and message number.
    # TODO 5: encode msg_id

    user: UserProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='messages')
    room: ChatRoom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    content: str = models.TextField(max_length=1000)
    msg_id: str = models.TextField(default='0', editable=False)

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # using = 'messages_db'
        ordering = ['-created_at']

    def save(self, *args, **kw) -> None:
        # Creating msg_id key and calling super().save method
        self.msg_id = f'{self.room.pk}-{self.user.pk}-{self.get_msg_count() + 1}'
        super().save(self, *args, **kw)

    def __str__(self) -> str:
        return f'Message <{self.msg_id}>'

    def get_message(self) -> str:
        return self.content

    def get_sender_id(self) -> int | Any:
        return self.user.pk

    def get_sender_name(self) -> str:
        return self.user.username

    def get_room_id(self) -> int | Any:
        return self.room.pk

    @classmethod
    def get_msg_count(cls) -> int:
        return Message.objects.count() if not None else 0
