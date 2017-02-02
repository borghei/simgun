from django.http import JsonResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from django.urls import reverse

from accounts.models import UserProfile
from books.models import Book, BookReview
from profiles.models import WishlistBook, ShoppingbagBook, ReadingProgram


def add_to_wishlist(request, profile_id):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = get_object_or_404(Book, pk=book_id)
        user_profile = get_object_or_404(UserProfile, pk=profile_id)
        if WishlistBook.objects.filter(user_profile=user_profile, book=book).count() == 0:
            wishlist_book = WishlistBook(user_profile=user_profile, book=book)
            wishlist_book.save()
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'failure'})


def remove_from_wishlist(request, profile_id, wishlist_id):
    if request.method == 'POST':
        user_profile = get_object_or_404(UserProfile, pk=profile_id)
        wishlist_book = get_object_or_404(WishlistBook, pk=wishlist_id)
        wishlist_book.delete()
        return JsonResponse({'status': 'ok', 'url': reverse('profiles:wishlist', args=(profile_id,))})


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


def create_readingprogram(request, profile_id):
    if request.method == 'POST':
        book_id = request.POST.get('book_id', -1)
        if book_id == -1:
            return JsonResponse({'status': 'failure'})
        user_profile = get_object_or_404(UserProfile, pk=profile_id)
        # TODO check for golden User
        if user_profile.bookreview_set.all().count() > 0:
            return JsonResponse({
                'status': 'failure',
            })
        book = get_object_or_404(Book, pk=book_id)
        reading_program = ReadingProgram(user_profile=user_profile, book=book, current_page=0)
        reading_program.save()
        return JsonResponse({
            'status': 'ok',
            'url': reverse('profiles:readingprograms', args=(profile_id,))
        })


def update_readingprogram(request, profile_id, program_id):
    if request.method == 'POST':
        user_profile = get_object_or_404(UserProfile, pk=profile_id)
        reading_program = get_object_or_404(ReadingProgram, pk=program_id)
        page_id = int(request.POST.get('current_page', -1))
        if page_id > reading_program.current_page:
            reading_program.current_page = page_id
            reading_program.save()
            return JsonResponse({
                'status': 'ok',
                'url': reverse('profiles:readingprograms', args=(profile_id,))
            })
        else:
            return JsonResponse({'status': 'failure'})


def profile(request, profile_id, tab=1):
    user_profile = get_object_or_404(UserProfile, pk=profile_id)
    reading_programs = user_profile.readingprogram_set.all()
    favs = user_profile.wishlistbook_set.all()
    reviews = user_profile.bookreview_set.all()
    return render(request, 'profiles/profile.html', {
        'reading_programs': reading_programs,
        'favs': favs,
        'reviews': reviews,
        'user_profile': user_profile,
        'active_tab': tab,
    })


def view_readingprogram(request, profile_id, program_id):
    if request.method == 'GET':
        user_profile = get_object_or_404(UserProfile, pk=profile_id)
        reading_program = get_object_or_404(ReadingProgram, pk=program_id)
        book = reading_program.book
        return JsonResponse({
            'status': 'ok',
            'book_title': book.title,
            'book_page_count': book.page_count,
            'book_image': book.pic.url,
            'current_page': reading_program.current_page,
        })
    else:
        return JsonResponse({
            'status': 'failure'
        })


def remove_readingprogram(request, profile_id, program_id):
    user_profile = get_object_or_404(UserProfile, pk=profile_id)
    reading_program = get_object_or_404(ReadingProgram, pk=program_id)
    reading_program.delete()
    return JsonResponse({'status': 'ok', 'url': reverse('profiles:readingprograms', args=(profile_id,))})


def wishlist(request, profile_id):
    if request.method == 'GET':
        return profile(request, profile_id, 1)


def readingprograms(request, profile_id):
    if request.method == 'GET':
        return profile(request, profile_id, 2)


def reviews(request, profile_id):
    if request.method == 'GET':
        return profile(request, profile_id, 3)


def remove_review(request, profile_id, review_id):
    user_profile = get_object_or_404(UserProfile, pk=profile_id)
    review = get_object_or_404(BookReview, pk=review_id)
    review.delete()
    print(reverse('profiles:reviews', args=(profile_id,)))
    return JsonResponse({'status': 'ok', 'url': reverse('profiles:reviews', args=(profile_id,))})


def remove_wishlist_book(request, profile_id):
    if request.method == 'POST':
        user_profile = get_object_or_404(UserProfile, pk=profile_id)
        book_id = request.POST.get('book_id', -1)
        if book_id == -1:
            return JsonResponse({'status': 'failure'})
        book = get_object_or_404(Book, pk=book_id)
        wishlist = get_object_or_404(WishlistBook, user_profile=user_profile, book=book)
        wishlist.delete()
        return JsonResponse({'status': 'ok', 'url': reverse('profiles:wishlist', args=(profile_id,))})


def settings(request, profile_id):
    if request.method == 'GET':
        user_profile = get_object_or_404(UserProfile, pk=profile_id)
        return render(request,'profiles/settings.html',{
            'user_profile': user_profile,

        })
    elif request.method == 'POST':
        return None


def upgrade_user(request, profile_id):
    return render(request, 'profiles/premium-membership.html')