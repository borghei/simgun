from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from profiles import views

app_name = 'profiles'
urlpatterns = [
    url(r'^(?P<profile_id>[0-9]+)/$', login_required(views.profile),
        name='profile'),
    url(r'^(?P<profile_id>[0-9]+)/settings/$', login_required(views.settings),
        name='settings'),
    url(r'^(?P<profile_id>[0-9]+)/upgrade/$', login_required(views.upgrade_user),
        name='upgrade_user'),
    url(r'^(?P<profile_id>[0-9]+)/wishlists/$', login_required(views.wishlist),
        name='wishlist'),
    url(r'^(?P<profile_id>[0-9]+)/wishlists/add/$', login_required(views.add_to_wishlist),
        name='add_wishlist'),
    url(r'^(?P<profile_id>[0-9]+)/wishlists/(?P<wishlist_id>[0-9]+)/remove/$', login_required(views.remove_from_wishlist),
        name='remove_wishlist'),
    url(r'^(?P<profile_id>[0-9]+)/wishlists/remove/$', login_required(views.remove_wishlist_book),
        name='remove_wishlist_book'),
    url(r'^(?P<profile_id>[0-9]+)/shoppingbag/$', login_required(views.shoppingbag),
        name='shoppingbag'),
    url(r'^(?P<profile_id>[0-9]+)/shoppingbag/add/$', login_required(views.add_to_shoppingbag),
        name='add_shoppingbag'),
    url(r'^(?P<profile_id>[0-9]+)/programs/$', login_required(views.readingprograms),
        name='readingprograms'),
    url(r'^(?P<profile_id>[0-9]+)/programs/add/$', login_required(views.create_readingprogram),
        name='create_readingprogram'),
    url(r'^(?P<profile_id>[0-9]+)/programs/(?P<program_id>[0-9]+)/$',
        login_required(views.view_readingprogram),
        name='view_readingprogram'),
    url(r'^(?P<profile_id>[0-9]+)/programs/(?P<program_id>[0-9]+)/update/$', login_required(views.update_readingprogram),
        name='update_readingprogram'),
    url(r'^(?P<profile_id>[0-9]+)/programs/(?P<program_id>[0-9]+)/remove/$', login_required(views.remove_readingprogram),
        name='remove_readingprogram'),
    url(r'^(?P<profile_id>[0-9]+)/reviews/$', login_required(views.reviews),
        name='reviews'),
    url(r'^(?P<profile_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)/remove/$', login_required(views.remove_review),
        name='remove_review'),

]
