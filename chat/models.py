from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ChatRoom(models.Model):
    name = models.CharField(max_length=100)
    # room_host = models.OneToOneField(User, on_delete=models.CASCADE)
    # room_members = models.ManyToManyField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self): # __str__ for Python 3, __unicode__ for Python 2
        return self.name


