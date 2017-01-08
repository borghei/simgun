# Create your views here.
from django.shortcuts import render
from django.views import generic

from ketabkhor.models import Book

def home_page(request):
    return render(request, "ketabkhor/index.html")


class BookDetails(generic.DetailView):
    model = Book
    template_name = "ketabkhor/book-detail.html"
