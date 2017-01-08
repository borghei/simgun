from django.conf.urls import url

from books import views


app_name = 'books'
urlpatterns = [
    url(r'^(?P<book_id>[0-9]+)/$', views.book_details, name='book_details'),
    url(r'^(?P<book_id>[0-9]+)/review/add/$', views.add_book_review, name='add_book_review'),
]

