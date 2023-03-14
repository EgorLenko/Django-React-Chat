from pymongo import MongoClient
from django.conf import settings
from djongo import models


def get_mongodb_handler(msg_host=settings.MSG_DB['HOST'],
                        msg_port=int(settings.MSG_DB['PORT']),
                        msg_username=settings.MSG_DB['USERNAME'],
                        msg_password=settings.MSG_DB['PASSWORD']):

    client = MongoClient(host=msg_host, port=msg_port, username=msg_username, password=msg_password)

    db = client[settings.MSG_DB['NAME']]

    return db, client


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='messages')
    room = models.ForeignKey('ChatRoom', on_delete=models.CASCADE, related_name='messages')
    content = models.TextField(max_length=1000)
    msg_id = models.TextField(default='0', editable=False)

    class Meta:
        # using = 'messages_db'
        ordering = ['-created_at']

    def save(self, *args, **kw):
        self.msg_id = f'{self.room.pk}-{self.user.pk}-{self.get_msg_count() + 1}'
        super().save(self, *args, **kw)

    def __str__(self) -> str:
        return f'Message {self.msg_id}'

    def get_message(self) -> str:
        return self.content

    def get_sender_id(self):
        return self.user.pk

    def get_sender_name(self) -> str:
        return self.user.username

    def get_room_id(self):
        return self.room.pk

    @classmethod
    def get_msg_count(cls):
        return Message.objects.count() if not None else 0
