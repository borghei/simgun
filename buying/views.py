from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from accounts.models import UserProfile, Vendor

from buying.models import Address

from .models import PostPrice


def order_info(request, user_id):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    adrs = user_profile.address_set.filter(validity=1).all()
    return render(request, 'buying/order-info.html', {"up": user_profile, 'adrs': adrs})


def get_post_price(request, user_id):
    vendor = get_object_or_404(Vendor, user=request.user)
    try:
        d = request.POST

        pp = vendor.postprice_set.filter(province=d['province'],
                            city=d['city'],
                            type=d['stype']).first()

        return JsonResponse({'stat': 1, 'price': pp.price})
    except:
        return JsonResponse({'stat': 0, 'price': 'این شهر قبلا ثبت نشده است.'})


def set_post_price(request, user_id):
    vendor = get_object_or_404(Vendor, user=request.user)
    try:
        d = request.POST

        pp = vendor.postprice_set.filter(province=d['province'],
                                         city=d['city'],
                                         type=d['stype'])

        if pp and pp.first():
            pp = pp.first()
            pp.price = d['price']
        else:
            pp = PostPrice(province=d['province'],
                           city=d['city'],
                           type=d['stype'],
                           vendor=vendor,
                           price=d['price']
                           )

        pp.save()
        return JsonResponse({'stat': 1})
    except:
        return JsonResponse({'stat': 0})


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

