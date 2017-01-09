from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render


def search(request):
    query = request.GET['q']
    return render(request, 'search/advanced-search.html', {
        'query': query,
    })
