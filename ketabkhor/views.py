from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render


def book_details(request, isbn):
    print(isbn)
    return HttpResponse(" ISBN: ")


def home_page(request):
    return render(request, "ketabkhor/index.html")
