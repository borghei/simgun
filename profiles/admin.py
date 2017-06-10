from django.contrib import admin

# Register your models here.
from profiles.models import Bag, ShoppingbagProduct#, ReadingProgram

admin.site.register(Bag)
admin.site.register(ShoppingbagProduct)
# admin.site.register(ReadingProgram)#