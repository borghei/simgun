from django.conf.urls import url

from books import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.BookDetails.as_view(), name='book_details'),
    url(r'^(?P<book_id>[0-9]+)/review/add/$', views.add_book_review, name='add_book_review'),
]

