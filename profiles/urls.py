from django.conf.urls import url, include

from profiles import views


app_name = 'profiles'
urlpatterns = [
    url(r'^(?P<profile_id>[0-9]+)/wishlist/add/$', views.add_to_wishlist, name='add_wishlist'),
]
