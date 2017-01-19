from django.conf.urls import url

from buying import views

app_name = 'buying'
urlpatterns = [
    url(r'(?P<user_id>[0-9]+)/', views.order_info, name='order_info'),
]
