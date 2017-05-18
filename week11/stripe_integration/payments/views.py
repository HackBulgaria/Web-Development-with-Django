from django.views import View
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from .tasks import create_customer


class CreateCustomerView(LoginRequiredMixin, View):
    def get_success_url(self):
        return reverse('magazine:magazine-list')

    def post(self, request, *args, **kwargs):
        token = request.POST['stripeToken']
        create_customer.delay(card_token=token, buyer_id=request.user.id)

        return redirect(self.get_success_url())


class ChargeCustomerView(LoginRequiredMixin, View):
    def get_success_url(self):
        return reverse('magazine:magazine-list')

    def post(self, request, *args, **kwargs):
        print("Make charge here. Use celery.")
        print("Create CustomerCharge model. Keep charge ids there. Use the to Refund.")
        return redirect(self.get_success_url())
