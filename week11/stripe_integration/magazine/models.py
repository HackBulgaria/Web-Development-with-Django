from django.db import models

from users.models import Author


class Magazine(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    magazine = models.ForeignKey(Magazine)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    author = models.ForeignKey(Author)

    def __str__(self):
        return "{} for {}".format(self.name, self.magazine)
