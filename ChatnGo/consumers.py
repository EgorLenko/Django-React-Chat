"""Websocket configuration module."""
import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model

from django.core import serializers

from ChatnGo.views.views import ChatRoom, Message

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    """Websocket consumer for chat application"""

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None
        self.room_group_name = None

    @database_sync_to_async
    def save_message(self, username, message):
        user = User.objects.get(username=username)
        chat_room = ChatRoom.objects.get(name=self.room_name)
        Message.objects.create(user=user, content=message, room=chat_room)

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['roomId']
        self.room_group_name = f"chat_{self.room_name}"
        print(f"Connecting to {self.room_name}")
        print(f"Parameters:\n {self.room_name=}, {self.room_group_name=}")
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        await super().disconnect(close_code)

    async def receive(self, text_data=None, bytes_data=None):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json["message"]
            username = text_data_json["username"]

            # Save message to database
            await self.save_message(username, message)

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {"type": "chat_message", "message": message, "username": username},
            )

        except (TypeError, json.decoder.JSONDecodeError) as err:
            print(f"Catch an Exception <{err.__class__.__name__}>:\n {err}")
            await self.send(text_data=json.dumps({"error": "Invalid message"}))

    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        print('=========Event check=====================')
        print(f'{username=}, {message=}')
        print('=========Event check=====================')

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps({"message": message, "username": username})
        )

    async def load_messages(self, event):
        messages = Message.objects.filter(room=self.room_name).order_by("-created_at")[:10]
        messages_serialized = serializers.serialize("json", messages)  # Or Message.serializer (Not sure)

        # Send messages to WebSocket
        await self.send(text_data=json.dumps({"messages": messages_serialized}))

    async def load_users(self, event):
        users = User.objects.filter(rooms=self.room_name)
        users_serialized = serializers.serialize("json", users)

        # Send users to WebSocket
        await self.send(text_data=json.dumps({"users": users_serialized}))
