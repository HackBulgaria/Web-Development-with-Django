import factory
from .models import Tag, BlogPost
from faker import Factory

faker = Factory.create()


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.LazyAttribute(lambda _: faker.word())


class BlogPostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BlogPost

    title = factory.LazyAttribute(lambda _: faker.word())

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for group in extracted:
                self.tags.add(group)
