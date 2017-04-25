import uuid
from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(unique=True, max_length=255)


class Product(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(unique=True, max_length=255)

    comments = models.ManyToManyField(User, through='comments.Comment')
    categories = models.ManyToManyField(Category, related_name='products')
