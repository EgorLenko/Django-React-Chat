import json

from .views import *

from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from django.core import serializers
from .models import Message

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.chat_room_name = None
        self.chat_room_group_name = None

    async def connect(self):
        self.chat_room_name = self.scope['url_route']['kwargs']['room_name']
        self.chat_room_group_name = f'chat_{self.chat_room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.chat_room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.chat_room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        user = User.objects.get(username=username)
        chat_room = ChatRoom.objects.get(name=self.chat_room_name)

        # Save message to MongoDB
        msg = Message(text=message, user=user, chat_room=chat_room)
        msg.save()

        # Send message to room group
        await self.channel_layer.group_send(
            self.chat_room_group_name,
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
        messages = Message.objects.filter(chat_room__name=self.chat_room_name).order_by('-created_at')[:10]
        messages_serialized = serializers.serialize('json', messages)

        # Send messages to WebSocket
        await self.send(text_data=json.dumps({
            'messages': messages_serialized
        }))

    async def load_users(self, event):
        users = User.objects.filter(chatroom__name=self.chat_room_name)
        users_serialized = serializers.serialize('json', users)

        # Send users to WebSocket
        await self.send(text_data=json.dumps({
            'users': users_serialized
        }))
