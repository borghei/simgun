from random import randint

from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from accounts.models import UserProfile
from product.models import Product, Review, Rating


def random(query_set):
    count = query_set.aggregate(count=Count('id'))['count']
    random_index = randint(0, count - 1)
    return query_set.all()[random_index]

#TODO too large method
def book_details(request, book_id):
    book = get_object_or_404(Product, pk=book_id)
    related_books = book.category.book_set.exclude(pk=book_id)
    # related_books = random(related_books)
    #TODO this method is very slow
    related_books = related_books.order_by('?')[0:4]
    all_bookratings = book.bookrating_set.all()
    user = request.user
    user_profile = None
    if user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=user)
        book_rate = user_profile.bookrating_set.filter(book=book)
        if book_rate.count() > 0:
            user_book_rate = book_rate[0].rate
        else:
            user_book_rate = 0
    else:
        user_book_rate = 0
    if all_bookratings.count() == 0:
        book_rate_avg = 0
    else:
        book_rate_avg = book.get_avg_rating()
    return render(request, 'books/book-detail.html', {
        'book': book,
        'related_books': related_books,
        'book_rate': book_rate_avg,
        'user_book_rate': user_book_rate,
        'user_profile': user_profile,
    })


def add_book_review(request, book_id):
    if request.method == 'POST':
        if request.POST.get('text').strip() == '':
            return JsonResponse({'status': 'failure'})

        book = get_object_or_404(Product, pk=book_id)
        user_profile = get_object_or_404(UserProfile, user=request.user)

        book_review = Review(user_profile=user_profile,
                             book=book,
                             text=request.POST.get('text'))
        book_review.save()
        return JsonResponse({'status': 'ok', 'url': reverse('product:book_details', args=(book_id, ))})
    else:
        return JsonResponse({'status': 'failure'})


def rate_book(request, book_id):
    #TODO check if rate is not empty
    if request.method == 'POST':
        rate = request.POST.get('rate', -1)
        if rate == -1:
            return JsonResponse({'status': 'failure'})
        book = get_object_or_404(Product, pk=book_id)
        user_profile = get_object_or_404(UserProfile, user=request.user)
        book_rate, created = Rating.objects.get_or_create(
            book=book,
            user_profile=user_profile
        )
        book_rate.rate = rate
        book_rate.save()
        return JsonResponse({'status': 'ok', 'url': reverse('product:book_details', args=(book_id,))})
    else:
        return JsonResponse({'status': 'failure'})
