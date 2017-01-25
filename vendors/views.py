from django.db.models import Count
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from accounts.models import Vendor, UserProfile
from books.models import Book
from vendors.models import BookVendor, ShoppingbagVendor


def vendor_profile(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    orders = ShoppingbagVendor.objects.values('user_profile').distinct()
    return render(request, 'vendors/vendor-profile.html', {'vendor': vendor, 'orders': orders})


def add_book(request, vendor_id):
    if request.method == 'POST':
        vendor = get_object_or_404(Vendor, pk=vendor_id)
        isbn = request.POST['isbn']
        book = Book.objects.filter(isbn=isbn)
        if book.count() == 0:
            book = Book(
                isbn=request.POST['isbn'],
                title=request.POST['title'],
                author=request.POST['author'],
                translator=request.POST.get('translator', ''),
                description=request.POST['description'],
                page_count=request.POST['page_count'],
                publisher=request.POST['publisher'],
                price=request.POST['price'],
                pic=request.FILES.get('pic'),
                #TODO add tags to the book
            )
            book.save()
        book_vendor = BookVendor(vendor=vendor, book=book)
        book_vendor.save()
        return HttpResponseRedirect(reverse('vendors:vendor_profile', args=(vendor_id,)))


def vendor_orders(request):
    return None