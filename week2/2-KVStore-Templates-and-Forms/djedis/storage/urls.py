from django.conf.urls import url

from .views import add_key


urlpatterns = [
    url(r'^add-key/(.*)/$', add_key),
]
