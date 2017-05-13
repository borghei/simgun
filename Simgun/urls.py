"""Simgun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from product.models import Product
from ketabkhor import views


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('isbn', 'title', 'author', 'translator')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = BookSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'product', BookViewSet)

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^admin/', admin.site.urls),
    url(r'^product/', include('product.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^vendors/', include('vendors.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^premium/', include('premium.urls')),
    url(r'^vendors/', include('vendors.urls')),
    url(r'^orders/', include('buying.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api/v1/', include('rest_framework.urls', namespace='rest_framework'))
]
