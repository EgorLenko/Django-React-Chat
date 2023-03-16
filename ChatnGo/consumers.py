import json

from django.core import serializers
from django.contrib.auth import get_user_model

from channels.generic.websocket import AsyncWebsocketConsumer

from .models import Message
from .views import *

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None
        self.room_group_name = None

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        await super().receive(text_data)  # ? TODO: Dont forget to remove this
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        user = User.objects.get(username=username)
        chat_room = ChatRoom.objects.get(name=self.room_name)

        # Save message to database
        msg = Message(user=user, content=message, room=chat_room)
        msg.save()

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    async def load_messages(self, event):
        messages = Message.objects.filter(room=self.room_name).order_by('-created_at')[:10]
        messages_serialized = serializers.serialize('json', messages)  # Or Message.serializer (Not sure)

        # Send messages to WebSocket
        await self.send(text_data=json.dumps({
            'messages': messages_serialized
        }))

    async def load_users(self, event):
        users = User.objects.filter(rooms=self.room_name)  # TODO 1: FIX IT!
        users_serialized = serializers.serialize('json', users)

        # Send users to WebSocket
        await self.send(text_data=json.dumps({
            'users': users_serialized
        }))
