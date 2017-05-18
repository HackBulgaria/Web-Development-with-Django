from django.conf.urls import url

from .views import CreateCustomerView, ChargeCustomerView


urlpatterns = [
    url(
        regex='^create-customer/$',
        view=CreateCustomerView.as_view(),
        name='create-customer'
    ),
    url(
        regex='^charge/$',
        view=ChargeCustomerView.as_view(),
        name='charge-customer'
    ),
]
