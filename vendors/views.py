from django.db.models import Count
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from accounts.models import Vendor, UserProfile
from product.models import Product, Category
from vendors.models import ProductVendor, ShoppingbagVendor


def vendor_profile(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    orders = ShoppingbagVendor.objects.values('user_profile').distinct()
    return render(request, 'vendors/vendor-profile.html', {'vendor': vendor, 'orders': orders})


def add_product(request, vendor_id):
    if request.method == 'POST':
        vendor = get_object_or_404(Vendor, pk=vendor_id)
        print(request.POST['price'])

        p = Product(
            title=request.POST['title'],
            description=request.POST['description'],
            itemCount=request.POST['itemCount'],
            category=Category.objects.get(title__contains=request.POST['category']),
            price=request.POST['price'],
            mainPic=request.FILES.get('mainPic'),
            weight=request.POST['weight']
        )

        p.save()
        product_vendor = ProductVendor(vendor=vendor, product=p)
        product_vendor.save()
        return HttpResponseRedirect(reverse('vendors:vendor_profile', args=(vendor_id,)))


def vendor_orders(request):
    return None