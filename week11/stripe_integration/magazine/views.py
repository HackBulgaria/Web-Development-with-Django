from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.conf import settings

from .models import Magazine, Article


class MagazineListview(LoginRequiredMixin, ListView):
    model = Magazine
    template_name = 'magazine/list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['stripe_pk'] = settings.STRIPE_PUBLIC_KEY

        return context


class ArticleListview(ListView):
    model = Article
    template_name = 'magazine/article_list.html'

    def get_queryset(self):
        return self.model.objects\
                         .filter(magazine_id=self.kwargs.get('magazine_id'))
