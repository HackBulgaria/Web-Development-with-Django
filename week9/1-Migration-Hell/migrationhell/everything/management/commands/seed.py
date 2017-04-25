from django.core.management.base import BaseCommand, CommandError

from faker import Factory

from everything.models import (
    User,
    Product,
    Category,
    Order,
    Invoice,
    Comment
)

faker = Factory.create()


class Command(BaseCommand):
    help = 'Seeds with initial data'

    def handle(self, *args, **options):
        user1 = User.objects.create(email='1' + faker.email())
        user2 = User.objects.create(email='2' + faker.email())

        category = Category.objects.create(name=faker.word())

        product = Product.objects.create(name=faker.word())
        product.categories.add(category)

        comment1 = Comment.objects.create(user=user1,
                                          product=product,
                                          text=faker.text())

        order1 = Order.objects.create(user=user1)
        order1.products.add(product)

        order2 = Order.objects.create(user=user2)
        order2.products.add(product)

        invoice1 = Invoice.objects.create(order=order1,
                                          company_data=faker.company())

        invoice2 = Invoice.objects.create(order=order2,
                                          company_data=faker.company())
