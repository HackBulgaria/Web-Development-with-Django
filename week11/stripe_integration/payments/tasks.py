import stripe

from celery import task

from django.conf import settings

from users.models import Buyer


@task
def create_customer(card_token, buyer_id):
    stripe.api_key = settings.STRIPE_API_KEY

    buyer = Buyer.objects.get(id=buyer_id)

    customer = stripe.Customer.create(
        email=buyer.email,
        source=card_token,
    )

    buyer.customer_id = customer.id
    buyer.save()

    return buyer.id
