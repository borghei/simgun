from django.db.models import Count
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from accounts.models import Vendor, UserProfile
from product.models import Product, Category
from vendors.models import ProductVendor
from profiles.models import ShoppingbagProduct
from .forms import AddProductForm


def vendor_profile(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    all_sb = ShoppingbagProduct.objects.filter(product__productvendor__vendor=vendor).all()

    orders = list(s for s in all_sb if s.bag.address and s.status != -1)

    delivered = [o for o in orders if o.status == 3]
    undelivered = [o for o in orders if o.status == -2]
    orders = [o for o in orders if o.status not in [-2, 3]]

    return render(request, 'vendors/vendor-profile.html',
                  {'vendor': vendor, 'orders': orders, 'delivered': delivered, 'undelivered': undelivered})


def add_product(request, vendor_id):
    if request.method == 'POST':

        vendor = get_object_or_404(Vendor, pk=vendor_id)
        print(request.POST)
        try:
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
        except:
            vendor = get_object_or_404(Vendor, pk=vendor_id)
            orders = None #ShoppingbagVendor.objects.values('user_profile').distinct()
            return render(request, 'vendors/vendor-profile.html', {'vendor': vendor, 'orders': orders})


def vendor_orders(request):
    return None