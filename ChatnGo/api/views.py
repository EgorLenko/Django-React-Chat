from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated

from ..models import ChatRoom, Message, UserProfile
from ..serializers import UserSerializer, ChatRoomSerializer, MessageSerializer


class UserList(generics.ListCreateAPIView):
    # Boilerplate for permission system:
    # permission_classes = [IsAuthenticated]
    #
    # def get_queryset(self):
    #     return UserProfile.objects.filter(user=self.request.user)
    #
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class MessageList(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class ChatRoomList(generics.ListCreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer


class ChatRoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
