from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

# Create your views here.
from accounts.models import UserProfile
from books.models import Book
from profiles.models import WishlistBook


def add_to_wishlist(request, profile_id):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = get_object_or_404(Book, pk=book_id)
        user = get_object_or_404(User, pk=profile_id)
        user_profile = get_object_or_404(UserProfile, user=user)
        if WishlistBook.objects.filter(user_profile=user_profile, book=book).count() == 0:
            wishlist_book = WishlistBook(user_profile=user_profile, book=book)
            wishlist_book.save()
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'failure'})


def remove_from_wishlist(request, profile_id):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = get_object_or_404(Book, pk=book_id)
        user = get_object_or_404(User, pk=profile_id)
        user_profile = get_object_or_404(UserProfile, user=user)
        wishlist_book = WishlistBook.objects.filter(user_profile=user_profile, book=book)
        if wishlist_book.count() == 0:
            return JsonResponse({'status': 'failure'})
        else:
            wishlist_book.delete()
            return JsonResponse({'status': 'ok'})


def add_to_shoppingbag(request):
    return None