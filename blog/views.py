from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.
from blog.models import Post


def blog_home_page(request):
    posts = get_list_or_404(Post.objects.all())
    return render(request, 'blog/blog-home.html', {
        'posts': posts
    })


def blog_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return HttpResponse("post %s" % post)
