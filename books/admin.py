from django.contrib import admin

from books.models import Book, BookReview, BookCategory


admin.site.register(BookCategory)
admin.site.register(Book)
admin.site.register(BookReview)