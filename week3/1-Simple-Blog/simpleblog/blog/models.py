from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)


class BlogPost(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=255, unique=True)

    tags = models.ManyToManyField(Tag,
                                  related_name='posts')

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()

        super().save(*args, **kwargs)
