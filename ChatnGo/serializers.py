from rest_framework import serializers
from .models import ChatRoom, Message, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
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
        fields = ('id', 'name', 'members')

    def create(self, validated_data):
        return ChatRoom.objects.create(**validated_data)


class MessageSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)  # serializers.StringRelatedField()
    # room = ChatRoomSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'user', 'room', 'content')

    def create(self, validated_data):
        return Message.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
