from django.conf.urls import url

from .apis import UniversalTruth

urlpatterns = [
    url(r'^truth/$', UniversalTruth.as_view()),
]
