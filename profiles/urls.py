from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from profiles import views

app_name = 'profiles'
urlpatterns = [
    url(r'^(?P<profile_id>[0-9]+)/', login_required(views.profile),
        name='profile'),
    url(r'^(?P<profile_id>[0-9]+)/wishlist/add/$', login_required(views.add_to_wishlist),
        name='add_wishlist'),
    url(r'^(?P<profile_id>[0-9]+)/wishlist/remove/$', login_required(views.remove_from_wishlist),
        name='remove_wishlist'),
    url(r'^(?P<profile_id>[0-9]+)/shoppingbag/$', login_required(views.shoppingbag),
        name='shoppingbag'),
    url(r'^(?P<profile_id>[0-9]+)/shoppingbag/add/$', login_required(views.add_to_shoppingbag),
        name='add_shoppingbag'),
    url(r'^(?P<profile_id>[0-9]+)/programs/$', login_required(views.readingprograms),
        name='readingprograms'),
    url(r'^(?P<profile_id>[0-9]+)/programs/add/', login_required(views.create_readingprogram),
        name='create_readingprogram'),
    url(r'^(?P<profile_id>[0-9]+)/programs/(?P<program_id>[0-9]+)/', login_required(views.update_readingprogram),
        name='update_readingprogram'),
]
