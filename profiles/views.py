from django.http import JsonResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from django.urls import reverse

from accounts.models import UserProfile
from product.models import Product, Review
from profiles.models import ShoppingbagProduct, Bag
from buying.models import Address

# def add_to_wishlist(request, profile_id):
#     if request.method == 'POST':
#         book_id = request.POST.get('book_id')
#         book = get_object_or_404(Product, pk=book_id)
#         user_profile = get_object_or_404(UserProfile, pk=profile_id)
#         if WishlistBook.objects.filter(user_profile=user_profile, book=book).count() == 0:
#             wishlist_book = WishlistBook(user_profile=user_profile, book=book)
#             wishlist_book.save()
#             return JsonResponse({'status': 'ok'})
#         else:
#             return JsonResponse({'status': 'failure'})


# def remove_from_wishlist(request, profile_id, wishlist_id):
#     if request.method == 'POST':
#         user_profile = get_object_or_404(UserProfile, pk=profile_id)
#         wishlist_book = get_object_or_404(WishlistBook, pk=wishlist_id)
#         wishlist_book.delete()
#         return JsonResponse({'status': 'ok', 'url': reverse('profiles:wishlist', args=(profile_id,))})


# TODO if the book is not available ...
def add_to_shoppingbag(request, profile_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=request.POST.get('book_id'))
        user_profile = get_object_or_404(UserProfile, user=request.user)
        try:
            last_bag = user_profile.bag_set.order_by('-date')[0]
            if last_bag.status == 1:
                last_bag = Bag(user_profile=user_profile)
        except:
            last_bag = Bag(user_profile=user_profile)
        last_bag.save()


        if not last_bag.shoppingbagproduct_set.filter(product=product):
            shoppingbag_product = ShoppingbagProduct(bag=last_bag, product=product, product_count=1, price=product.get_cost())
            shoppingbag_product.save()
            return JsonResponse({'status': 'ok',
                                 'url': reverse('profiles:shoppingbag', args=(profile_id,))
                                 })
        else:
            selected_shoppingbag_product = last_bag.shoppingbagproduct_set.get(product=product)
            selected_shoppingbag_product.product_count += 1
            selected_shoppingbag_product.save()
            return JsonResponse({'status': 'ok',
                                 'url': reverse('profiles:shoppingbag', args=(profile_id,))
                                 })


def shoppingbag(request, profile_id):
    if request.method == 'GET':
        user_profile = get_object_or_404(UserProfile, user=request.user)
        try:
            bags = user_profile.bag_set.all()
        except:
            bags = None
        return render(request, 'profiles/bags.html', {
            'bags': bags,
        })


def shoppingbag_spec(request, profile_id, bag_id):
    if request.method == 'GET':
        user_profile = get_object_or_404(UserProfile, user=request.user)
        try:
            shoppingbags = user_profile.bag_set.get(pk=bag_id)
        except:
            shoppingbags = None

        return render(request, 'profiles/shopping-bag.html', {
            'bag': shoppingbags
        })
# def create_readingprogram(request, profile_id):
#     if request.method == 'POST':
#         book_id = request.POST.get('book_id', -1)
#         if book_id == -1:
#             return JsonResponse({'status': 'failure'})
#         user_profile = get_object_or_404(UserProfile, pk=profile_id)
#         # TODO check for golden User
#         if user_profile.bookreview_set.all().count() > 0:
#             return JsonResponse({
#                 'status': 'failure',
#             })
#         book = get_object_or_404(Product, pk=book_id)
#         reading_program = ReadingProgram(user_profile=user_profile, book=book, current_page=0)
#         reading_program.save()
#         return JsonResponse({
#             'status': 'ok',
#             'url': reverse('profiles:readingprograms', args=(profile_id,))
#         })


# def update_readingprogram(request, profile_id, program_id):
#     if request.method == 'POST':
#         user_profile = get_object_or_404(UserProfile, pk=profile_id)
#         reading_program = get_object_or_404(ReadingProgram, pk=program_id)
#         page_id = int(request.POST.get('current_page', -1))
#         if page_id > reading_program.current_page:
#             reading_program.current_page = page_id
#             reading_program.save()
#             return JsonResponse({
#                 'status': 'ok',
#                 'url': reverse('profiles:readingprograms', args=(profile_id,))
#             })
#         else:
#             return JsonResponse({'status': 'failure'})


def profile(request, profile_id, tab=1):
    user_profile = get_object_or_404(UserProfile, pk=profile_id)
    # reading_programs = user_profile.readingprogram_set.all()
    # favs = user_profile.wishlistbook_set.all()
    # reviews = user_profile.bookreview_set.all()
    return render(request, 'profiles/profile.html', {
        # 'reading_programs': reading_programs,
        # 'favs': favs,
        # 'reviews': reviews,
        'user_profile': user_profile,
        'active_tab': tab,
    })


# def view_readingprogram(request, profile_id, program_id):
#     if request.method == 'GET':
#         user_profile = get_object_or_404(UserProfile, pk=profile_id)
#         reading_program = get_object_or_404(ReadingProgram, pk=program_id)
#         book = reading_program.book
#         return JsonResponse({
#             'status': 'ok',
#             'book_title': book.title,
#             'book_page_count': book.page_count,
#             'book_image': book.pic.url,
#             'current_page': reading_program.current_page,
#         })
#     else:
#         return JsonResponse({
#             'status': 'failure'
#         })
#
#
# def remove_readingprogram(request, profile_id, program_id):
#     user_profile = get_object_or_404(UserProfile, pk=profile_id)
#     reading_program = get_object_or_404(ReadingProgram, pk=program_id)
#     reading_program.delete()
#     return JsonResponse({'status': 'ok', 'url': reverse('profiles:readingprograms', args=(profile_id,))})


def set_address(request, profile_id):
    if request.method == 'POST':
        address = get_object_or_404(Address, pk=request.POST.get('selected_address'))
        user_profile = get_object_or_404(UserProfile, user=request.user)

        try:
            last_bag = user_profile.bag_set.order_by('-date')[0]
            if last_bag.status == 0:
                last_bag.address = address
                last_bag.save()
                for sb in last_bag.shoppingbagproduct_set.all():
                    if sb.product.productvendor_set.first().vendor.postprice_set.filter(province=address.province, city=address.city).count() == 0:
                        sb.status = -1
                        sb.save()
            return JsonResponse({'success': 1, 'url': reverse('profiles:shoppingbag_spec', args=(profile_id, last_bag.id))})


        except:
            return JsonResponse({'success': 1, 'url': reverse('profiles:shoppingbag', args=(profile_id, ))})




def comp_shopp(request, profile_id):
    if request.method == 'POST':
        user_profile = get_object_or_404(UserProfile, user=request.user)

        try:
            last_bag = user_profile.bag_set.order_by('-date')[0]
            if last_bag.status == 0:
                last_bag.status = 1
                last_bag.save()
                # for sb in last_bag.shoppingbagproduct_set.all():
                #     if sb.product.productvendor_set.first().vendor.postprice_set.filter(province=address.province, city=address.city).count() == 0:
                #         sb.status = -1
                #         sb.save()
            return JsonResponse({'success': 1})


        except:
            return JsonResponse({'success': 1})




def wishlist(request, profile_id):
    if request.method == 'GET':
        return profile(request, profile_id, 1)


# def readingprograms(request, profile_id):
#     if request.method == 'GET':
#         return profile(request, profile_id, 2)


def reviews(request, profile_id):
    if request.method == 'GET':
        return profile(request, profile_id, 3)


def remove_review(request, profile_id, review_id):
    user_profile = get_object_or_404(UserProfile, pk=profile_id)
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    print(reverse('profiles:reviews', args=(profile_id,)))
    return JsonResponse({'status': 'ok', 'url': reverse('profiles:reviews', args=(profile_id,))})


# def remove_wishlist_book(request, profile_id):
#     if request.method == 'POST':
#         user_profile = get_object_or_404(UserProfile, pk=profile_id)
#         book_id = request.POST.get('book_id', -1)
#         if book_id == -1:
#             return JsonResponse({'status': 'failure'})
#         book = get_object_or_404(Product, pk=book_id)
#         wishlist = get_object_or_404(WishlistBook, user_profile=user_profile, book=book)
#         wishlist.delete()
#         return JsonResponse({'status': 'ok', 'url': reverse('profiles:wishlist', args=(profile_id,))})


def settings(request, profile_id):
    user_profile = get_object_or_404(UserProfile, pk=profile_id)
    if request.method == 'GET':
        return render(request, 'profiles/settings.html', {
            'user_profile': user_profile,
        })
    elif request.method == 'POST':
        error_msgs = []
        user_profile.user.first_name = request.POST.get('first_name', user_profile.user.first_name)
        user_profile.user.last_name = request.POST.get('last_name', user_profile.user.last_name)
        user_profile.user.email = request.POST.get('email', user_profile.user.email)
        current_password = request.POST.get('current_password', '')
        if current_password != '':
            if user_profile.user.check_password(current_password):
                new_password = request.POST.get('new_password', '')
                new_password_replay = request.POST.get('new_password_replay', '')
                if new_password != '' and new_password_replay != '':
                    if new_password == new_password_replay:
                        if len(new_password) > 6:
                            user_profile.user.set_password(new_password)
                        else:
                            error_msgs.append('رمز عبور جدید باید بیشتر از ۶ حرف باشد.')
                    else:
                        error_msgs.append('رمز عبور جدید و تکرار آن با هم هم‌خوانی ندارند.')
                else:
                    if new_password == '':
                        error_msgs.append('رمز عبور جدید خالی است.')
                    if new_password_replay == '':
                        error_msgs.append('تکرار رمز عبور جدید خالی است.')
            else:
                error_msgs.append('رمز عبور فعلی اشتباه وارد شده است.')

        return HttpResponseRedirect(reverse('profiles:settings', args=(profile_id,)))


def upgrade_user(request, profile_id):
    return render(request, 'profiles/premium-membership.html')