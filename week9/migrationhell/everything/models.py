import uuid

from django.db import models


class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True)


class Category(models.Model):
    name = models.CharField(unique=True, max_length=255)


class Product(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(unique=True, max_length=255)

    comments = models.ManyToManyField(User, through='Comment')
    categories = models.ManyToManyField(Category, related_name='products')


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments')
    product = models.ForeignKey(Product)
    text = models.TextField()


class Order(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, related_name='orders')
    products = models.ManyToManyField(Product)


class Invoice(models.Model):
    company_data = models.TextField()
    order = models.OneToOneField(Order)
