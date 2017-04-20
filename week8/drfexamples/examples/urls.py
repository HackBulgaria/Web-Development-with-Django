from django.conf.urls import url

from rest_framework_jwt.views import obtain_jwt_token

from .apis import UniversalTruth

urlpatterns = [
    url(r'^truth/$', UniversalTruth.as_view()),
    url(r'^login/', obtain_jwt_token),
]
