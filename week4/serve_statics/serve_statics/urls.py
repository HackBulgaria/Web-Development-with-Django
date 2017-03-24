from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('website.urls', namespace='website')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
