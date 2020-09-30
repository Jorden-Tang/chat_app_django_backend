from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class chatRoom (models.Model){
    room_name = models.CharField(max_length=100)
    room_host = models.OneToOneField(User, verbose_name=_(""), on_delete=models.CASCADE)
    room_members = models.ManyToManyField(User, verbose_name=_(""), on_delete=models.CASCADE)
    created_at = models.DateTimeField(_(""), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_(""), auto_now=True, auto_now_add=False)
}


