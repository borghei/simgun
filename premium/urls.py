from django.conf.urls import url

from premium import views

app_name = 'premium'
urlpatterns = [
    url(r'^$', views.premium, name='premium'),
]
