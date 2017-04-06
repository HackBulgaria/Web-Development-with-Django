import factory
from django.contrib.auth.models import User
from .models import Category, Offer
from faker import Factory

faker = Factory.create()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.LazyAttribute(lambda _: faker.word())


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda _: faker.name())
    password = 'Ivoepanda'


class OfferFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Offer

    title = factory.LazyAttribute(lambda _: faker.word())
    description = factory.LazyAttribute(lambda _: faker.text())

    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
    # image = factory.django.ImageField(filename=(lambda _: faker.name()))
