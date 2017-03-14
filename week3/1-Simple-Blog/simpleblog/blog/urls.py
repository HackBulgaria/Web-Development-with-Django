from django.conf.urls import url

from .views import index, create_blog_post


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^create/$', create_blog_post, name='create')
]
