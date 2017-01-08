from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic

from books.models import Book, BookReview


class BookDetails(generic.DetailView):
    model = Book
    template_name = "ketabkhor/book-detail.html"


def add_book_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    user_profile = get_object_or_404(Book, user=request.user)
    book_review = BookReview(user_profile=user_profile, book=book)
    book_review.save()
    return JsonResponse({'status': 'ok'})