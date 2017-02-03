from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def blog_home_page(request):
    return HttpResponse("home_page")


def blog_post(request, post_id):
    return HttpResponse("post")
