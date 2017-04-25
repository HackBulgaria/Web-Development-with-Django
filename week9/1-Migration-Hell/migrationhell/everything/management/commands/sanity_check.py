from django.core.management.base import BaseCommand, CommandError

from faker import Factory

# from everything.models import (
#     User,
#     Product,
#     Category,
#     Order,
#     Invoice,
#     Comment
# )
from users.models import User
from products.models import Category, Product
from comments.models import Comment
from cart.models import Order, Invoice

faker = Factory.create()


class Command(BaseCommand):
    help = 'Seeds with initial data'

    def handle(self, *args, **options):
        users = User.objects.values_list('uuid', 'email')
        categories = Category.objects.values_list('id', 'name')
        products = Product.objects.values_list('uuid', 'name')
        comments = Comment.objects.values_list('id', 'user', 'product', 'text')
        orders = Order.objects.values_list('uuid', 'user')
        invoices = Invoice.objects.values_list('id', 'company_data', 'order')

        product_to_categories = []
        orders_to_product = []

        for product in Product.objects.all():
            product_to_categories.append(repr(product.categories.values_list('id', 'name')))

        for order in Order.objects.all():
            orders_to_product.append(repr(order.products.values_list('uuid', 'name')))

        print(repr(users))
        print(repr(categories))
        print(repr(users))
        print(repr(products))
        print(repr(comments))
        print(repr(orders))
        print(repr(invoices))
        print('\n'.join(product_to_categories))
        print('\n'.join(orders_to_product))
