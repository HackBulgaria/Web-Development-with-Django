from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Magazine, Article


class MagazineListview(LoginRequiredMixin, ListView):
    model = Magazine
    template_name = 'magazine/list.html'


class ArticleListview(ListView):
    model = Article
    template_name = 'magazine/article_list.html'

    def get_queryset(self):
        return self.model.objects\
                         .filter(magazine_id=self.kwargs.get('magazine_id'))
