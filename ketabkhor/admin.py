from django.contrib import admin

# Register your models here.
from ketabkhor.models import Book, UserProfile

admin.site.register(Book)
admin.site.register(UserProfile)