from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import (
    BaseUserManager,
    AuthorManager,
    BuyerManager
)


class BaseUser(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(max_length=255,
                              unique=True,
                              verbose_name='email address')
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = BaseUserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email


class Author(BaseUser):
    age = models.IntegerField()
    interests = models.TextField(blank=True, null=True)

    objects = AuthorManager()


class Buyer(BaseUser):
    came_from = models.CharField(max_length=255, blank=True)
    customer_id = models.CharField(max_length=255, blank=True, null=True)

    objects = BuyerManager()
