from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ChatRoom(models.Model):
    name = models.CharField(max_length=100) 
    description = models.CharField(max_length=500, default="Enter Your Room Description")
    members = models.ManyToManyField(User,verbose_name="room members", related_name="members")
    room_host = models.ForeignKey(User, verbose_name="room host", related_name="room_host", on_delete=models.CASCADE, default="null")
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

class Message(models.Model):
    context = models.CharField(max_length=1000)
    sender = models.ForeignKey(User, verbose_name="message_sender", related_name="sender",  on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.context