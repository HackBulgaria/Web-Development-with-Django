import uuid

from django.db import models
from django.utils import timezone


class User(models.Model):
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4)

    created_at = models.DateTimeField(default=timezone.now)


class KeyValue(models.Model):
    key = models.CharField(max_length=255)
    value = models.TextField()
    user = models.ForeignKey(User, related_name='data')

    created_at = models.DateTimeField(default=timezone.now)
