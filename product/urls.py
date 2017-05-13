from django.conf.urls import url

from product import views


app_name = 'product'
urlpatterns = [
    url(r'^(?P<book_id>[0-9]+)/$', views.book_details, name='productDetailsUrl'),
    url(r'^(?P<book_id>[0-9]+)/review/add/$', views.add_book_review, name='addProductReviewUrl'),
    url(r'^(?P<book_id>[0-9]+)/rate/add/$', views.rate_book, name='addProductRateUrl'),
]

