from django.conf.urls import url

from .views import MagazineListview, ArticleListview


urlpatterns = [
    url(
        regex='^$',
        view=MagazineListview.as_view(),
        name='magazine-list'
    ),
    url(
        regex='^(?P<magazine_id>[0-9]+)$',
        view=ArticleListview.as_view(),
        name='article-list'
    )
]
