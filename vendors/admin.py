from django.contrib import admin

# Register your models here.
from vendors.models import ProductVendor, ShoppingbagVendor

admin.site.register(ProductVendor)
admin.site.register(ShoppingbagVendor)