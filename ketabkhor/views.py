# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views import generic

from ketabkhor.models import Book


def home_page(request):
    return render(request, "ketabkhor/index.html")


class BookDetails(generic.DetailView):
    model = Book
    template_name = "ketabkhor/books/book_details.html"
