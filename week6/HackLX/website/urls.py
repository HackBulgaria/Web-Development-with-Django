from django.conf.urls import url
from django.contrib.auth.views import login, logout
from .views import OfferListView, CreateOfferView, UpdateOfferView
from .old_views import index, add_offer, edit_offer, delete_offer, get_statistics

urlpatterns = [
    url(r'^$', OfferListView.as_view(), name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^add-offer/$', CreateOfferView.as_view(), name='add-offer'),
    url(r'^offer/edit/(?P<offer>[0-9]+)', UpdateOfferView.as_view(), name='edit-offer'),
    url(r'^delete/(?P<pk>[0-9]+)$', delete_offer, name='delete-offer'),
    url(r'^statistics/$', get_statistics, name='statistics'),
]
