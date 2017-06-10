from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from accounts.models import UserProfile

from buying.models import Address

def order_info(request, user_id):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    adrs = user_profile.address_set.filter(validity=1).all()
    return render(request, 'buying/order-info.html', {"up": user_profile, 'adrs': adrs})


def get_post_price(request, user_id):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    adrs = user_profile.address_set.filter(validity=1).all()
    return JsonResponse({'stat': 1, 'price': 1000})


def add_address(request, user_id):
    # print(type(request.POST['city']))
    user_profile = get_object_or_404(UserProfile, user=request.user)
    try:
        d = request.POST
        address = Address(province=d['province'],
                          city=d['city'],
                          address=d['address'],
                          zipcode=d['zipcode'],
                          phone_number=d['phone_number'],
                          user_profile=user_profile)

        address.save()
        return JsonResponse({'stat': 1, 'add_id': address.id})
    except:
        return JsonResponse({'stat': 0})

