from django.conf.urls import url

from accounts import views

app_name = 'accounts'
urlpatterns = [
    url(r'^register/$', views.user_register, name='user_register'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
]