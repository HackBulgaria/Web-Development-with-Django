from django.conf.urls import url, include
from django.contrib import admin

from .views import index_view


urlpatterns = [
    url(r'^$', index_view, name='index'),
]
