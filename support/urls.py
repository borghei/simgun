from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'support'
urlpatterns = [
    url('^agent/(?P<agent_id>[0-9]+)/$', login_required(views.agent_profile), name='agent_page'),
    # url('^(?P<vendor_id>[0-9]+)/add-book/$', login_required(views.add_product), name='add_product'),
    # url('^(?P<vendor_id>[0-9]+)/orders/$', login_required(views.vendor_orders), name='vendor_orders'),
]