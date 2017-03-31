from django.conf.urls import url

from .views import index, create_blog_post, login_view, profile_view


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/$', login_view, name='login'),
    url(r'^profile/$', profile_view, name='profile'),
    url(r'^create/$', create_blog_post, name='create')
]
