from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Offer, Category

class OfferListView(ListView):
    model = Offer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.count()

        return context

class CreateOfferView(LoginRequiredMixin, CreateView):
    model = Offer
    fields = ("title", "description", "category", "image")
    template_name = 'website/offer_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('website:index')


class UpdateOfferView(LoginRequiredMixin, UpdateView):
    model = Offer
    pk_url_kwarg = 'offer'
    fields = ("title", "description", "category")
    template_name = 'website/offer_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('website:index')
