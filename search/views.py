from django.db.models import Q
from django.shortcuts import render

from books.models import Book


def search(request):
    results, query = advanced_search(request)
    return render(request, 'search/advanced-search.html', {
        'title': "جستجو",
        'books': results,
        'form_data': query
    })


def build_advance_search_query(request):
    """Transforms request.GET to a new QueryDic object that will have no empty value"""
    query = request.GET.copy()
    # normalize query
    for q in list(query):
        value = query[q]
        value = value.strip()
        if not value:
            del query[q]
        else:
            query[q] = value
    return query


def advanced_search(request):
    # It's easier to store a dict of the possible lookups we want, where
    # the values are the keyword arguments for the actual query.
    qdict = {'q': 'title__contains',
             'isbn': 'isbn__contains',
             'author': 'author__contains',
             'translator': 'translator__contains',
             'publisher': 'publisher__contains',
             'category': 'category__contains',
             }

    query = build_advance_search_query(request)
    # Then we can do this all in one step instead of needing to call
    # 'filter' and deal with intermediate data structures.
    q_objs = [Q(**{qdict[k]: request.GET[k]}) for k in qdict.keys() if k in request.GET]

    search_results = Book.objects.select_related().filter(*q_objs)
    if 'min_price' in request.GET and 'max_price' in request.GET:
        search_results = search_results.filter(price__range=(request.GET['min_price'], request.GET['max_price']))
    return search_results, query
