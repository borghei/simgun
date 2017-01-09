from django.contrib import admin

from books.models import Book, BookReview

admin.site.register(Book)
admin.site.register(BookReview)