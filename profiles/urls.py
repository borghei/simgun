from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from profiles import views


app_name = 'profiles'
urlpatterns = [
    url(r'^(?P<profile_id>[0-9]+)/wishlist/add/$', login_required(views.add_to_wishlist), name='add_wishlist'),
]
