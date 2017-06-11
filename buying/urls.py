from django.conf.urls import url

from buying import views

app_name = 'buying'

urlpatterns = [
    url(r'(?P<user_id>[0-9]+)/shopping/$', views.order_info, name='order_info'),
    url(r'(?P<user_id>[0-9]+)/addaddress/$', views.add_address, name='add_address'),
    url(r'(?P<user_id>[0-9]+)/removeaddress/(?P<add_id>[0-9]+)/$', views.order_info, name='remove_address'),

    url(r'(?P<user_id>[0-9]+)/getpostprice/$', views.get_post_price, name='get_post_price'),
    url(r'(?P<user_id>[0-9]+)/setpostprice/$', views.set_post_price, name='set_post_price'),
]
