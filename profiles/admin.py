from django.contrib import admin

# Register your models here.
from profiles.models import WishlistBook, ShoppingbagBook#, ReadingProgram

admin.site.register(WishlistBook)
admin.site.register(ShoppingbagBook)
admin.site.register(ReadingProgram)#