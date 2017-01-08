from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views import generic

from accounts.models import UserProfile
from books.models import Book, BookReview


class BookDetails(generic.DetailView):
    model = Book
    template_name = "ketabkhor/book-detail.html"


def add_book_review(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=book_id)
        user_profile = get_object_or_404(UserProfile, user=request.user)
        print('text: ' + str(request.POST.get('text')))
        print('title: ' + str(request.POST.get('title')))
        book_review = BookReview(user_profile=user_profile,
                                 book=book,
                                 title=request.POST.get('title'),
                                 text=request.POST.get('text'))
        book_review.save()
        return JsonResponse({'status': 'ok', 'url': reverse('books:book_details', args=(book_id,))})
    else:
        return JsonResponse({'status': 'failure'})
