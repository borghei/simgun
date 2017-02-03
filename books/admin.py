from django.contrib import admin

from books.models import Book, BookReview, BookCategory, BookRating

admin.site.register(BookCategory)
admin.site.register(Book)
admin.site.register(BookReview)
admin.site.register(BookRating)