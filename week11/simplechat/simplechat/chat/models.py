from django.db import models


class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.IntegerField(default=2)
