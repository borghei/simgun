from django.contrib import admin

# Register your models here.
from profiles.models import Bag, ShoppingbagBook#, ReadingProgram

admin.site.register(Bag)
admin.site.register(ShoppingbagBook)
# admin.site.register(ReadingProgram)#