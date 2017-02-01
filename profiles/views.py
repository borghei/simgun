from django.http import JsonResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

# Create your views here.
from django.urls import reverse

from accounts.models import UserProfile
from books.models import Book
from profiles.models import WishlistBook, ShoppingbagBook, ReadingProgram


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


# TODO if the book is not available ...
def add_to_shoppingbag(request, profile_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=request.POST.get('book_id'))
        user_profile = get_object_or_404(UserProfile, user=request.user)
        temp_shoppingbag_book = ShoppingbagBook.objects.filter(user_profile=user_profile, book=book)
        if temp_shoppingbag_book.count() == 0:
            shoppingbag_book = ShoppingbagBook(user_profile=user_profile, book=book)
            shoppingbag_book.save()
            return JsonResponse({'status': 'ok',
                                 'url': reverse('profiles:shoppingbag', args=(profile_id,))
                                 })
        else:
            selected_shoppingbag_book = temp_shoppingbag_book.get(user_profile=user_profile, book=book)
            selected_shoppingbag_book.book_count += 1
            selected_shoppingbag_book.save()
            return JsonResponse({'status': 'ok',
                                 'url': reverse('profiles:shoppingbag', args=(profile_id,))
                                 })


def shoppingbag(request, profile_id):
    if request.method == 'GET':
        user_profile = get_object_or_404(UserProfile, user=request.user)
        shoppingbags = user_profile.shoppingbagbook_set.all()
        return render(request, 'profiles/shopping-bag.html', {
            'shoppingbags': shoppingbags,
        })


def readingprograms(request, profile_id):
    if request.method == 'GET':
        user_profile = get_object_or_404(UserProfile, pk=profile_id)
        reading_programs = user_profile.readingprogram_set.all()
        #TODO reading program data must be set


def create_readingprogram(request, profile_id):
    if request.method == 'POST':
        user_profile = get_object_or_404(UserProfile, user=request.user)
        book = get_object_or_404(Book, pk=request.POST['book_id'])
        current_page = request.POST['current_page']
        reading_program = ReadingProgram(user_profile=user_profile, book=book, current_page=current_page)
        reading_program.save()
        return HttpResponseRedirect(reverse('profiles:readingprograms', args=(profile_id,)))
