from django.conf.urls import url

from blog import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.blog_home_page, name='blog_home_page'),
    url(r'^(?P<post_id>[0-9]+)/$', views.blog_post, name='blog_post'),
]
