from django.conf.urls import url, include
from django.http import HttpResponse

from .views import index, fact


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^calculator/fact/$', fact, name='fact'),
]
