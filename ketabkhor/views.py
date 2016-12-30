# Create your views here.
from django.shortcuts import render, get_object_or_404

from ketabkhor.models import Book


def book_details(request, isbn):
    book = get_object_or_404(Book, pk=isbn)
    return render(request, "ketabkhor/books/book_details.html",  {'book': book})


def home_page(request):
    return render(request, "ketabkhor/index.html")
