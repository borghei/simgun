from random import randint

from django.db.models import Count
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views import generic

from accounts.models import UserProfile
from books.models import Book, BookReview, BookRating


def random(query_set):
    count = query_set.aggregate(count=Count('id'))['count']
    random_index = randint(0, count - 1)
    return query_set.all()[random_index]


def book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    related_books = book.category.book_set.exclude(pk=book_id)
    # related_books = random(related_books)
    #TODO this method is very slow
    related_books = related_books.order_by('?')[0:4]
    return render(request, 'ketabkhor/book-detail.html', {
        'book': book,
        'related_books': related_books
    })


def add_book_review(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=book_id)
        user_profile = get_object_or_404(UserProfile, user=request.user)
        book_review = BookReview(user_profile=user_profile,
                                 book=book,
                                 title=request.POST.get('title'),
                                 text=request.POST.get('text'))
        book_review.save()
        # book = get_object_or_404(Book, pk=book_id)
        # related_books = book.category.book_set.exclude(pk=book_id)
        # related_books = related_books.order_by('?')[0:4]
        return JsonResponse({'status': 'ok', 'url': reverse('books:book_details', args=(book_id, ))})
    else:
        return JsonResponse({'status': 'failure'})


def rate_book(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=book_id)
        user_profile = get_object_or_404(UserProfile, user=request.user)
        book_rate = BookRating(book=book, user_profile=user_profile, rate=request.POST.get('rate'))
        book_rate.save()
        return JsonResponse({'status': 'ok', 'url': reverse('books:book_details', args=(book_id,))})
    else:
        return JsonResponse({'status': 'failure'})
