from django.contrib import admin

# Register your models here.
from vendors.models import BookVendor, ShoppingbagVendor

admin.site.register(BookVendor)
admin.site.register(ShoppingbagVendor)