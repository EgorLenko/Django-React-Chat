from rest_framework import serializers
from .models.models import ChatRoom
from .models.profile.user_profile import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'online')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user


class ChatRoomSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True)

    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'members']


# class MessageSerializer(serializers.ModelSerializer):
#     user = UserSerializer()  # serializers.StringRelatedField()
#     room = ChatRoomSerializer(read_only=True)
#
#     class Meta:
#         model = Message
#         fields = ['id', 'msg_id', 'user', 'room', 'content', 'created_at']
