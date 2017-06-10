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

    url(r'^(?P<profile_id>[0-9]+)/shoppingbag/$', login_required(views.shoppingbag),
        name='shoppingbag'),
    url(r'^(?P<profile_id>[0-9]+)/shoppingbag/(?P<bag_id>[0-9]+)/$', login_required(views.shoppingbag_spec),
        name='shoppingbag_spec'),
    url(r'^(?P<profile_id>[0-9]+)/shoppingbag/add/$', login_required(views.add_to_shoppingbag),
        name='add_shoppingbag'),
    url(r'^(?P<profile_id>[0-9]+)/shoppingbag/setaddress/', login_required(views.set_address),
        name='set_address'),
    url(r'^(?P<profile_id>[0-9]+)/shoppingbag/complete/', login_required(views.comp_shopp),
        name='comp_shopping'),
    url(r'^(?P<profile_id>[0-9]+)/reviews/$', login_required(views.reviews),
        name='reviews'),
    url(r'^(?P<profile_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)/remove/$', login_required(views.remove_review),
        name='remove_review'),

]
