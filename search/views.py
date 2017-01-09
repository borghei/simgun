from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

from books.models import Book


def search(request):
    title = request.GET['q']
    books = Book.objects.filter(title__contains=title)
    return render(request, 'search/advanced-search.html', {
        'title': title,
        'books': books
    })
