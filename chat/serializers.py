from rest_framework import serializers

from chat.models import ChatRoom
from django import forms

class PostSerializer (serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = (
            'name', 'description', 'members', 'room_host', 'created_at', 'updated_at'
        ) 