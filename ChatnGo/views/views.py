from rest_framework import generics
from ..models.models import ChatRoom
from ..models.profile.user_profile import UserProfile
from ..serializers import UserSerializer, ChatRoomSerializer


class UserList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


# ? INFO: Deprecated because of migration from Postgres to MongoDB (might come in handy later)

# class MessageList(generics.ListCreateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#
#
# class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer


class ChatRoomList(generics.ListCreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer


class ChatRoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
