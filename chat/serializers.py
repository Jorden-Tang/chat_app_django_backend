from rest_framework import serializers
from chat.models import ChatRoom
from django.contrib.auth.models import User
from django import forms
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class ChatRoomSerializer (serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = (
            'name', 'description', 'members', 'room_host', 'created_at', 'updated_at'
        )
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.name
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = ChatRoomSerializer



