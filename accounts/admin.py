from django.contrib import admin

# Register your models here.
from accounts.models import UserProfile, Vendor

admin.site.register(UserProfile)
admin.site.register(Vendor)