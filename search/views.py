from django.db.models import Q
from django.shortcuts import render

from books.models import Book


def search(request):
    title, results, query = advanced_search(request)
    if not results:
        return render(request, 'search/advanced-search-404.html', {
            'title': title})

    return render(request, 'search/advanced-search.html', {
        'title': title,
        'books': results,
        'form_data': query
    })


def advanced_search(request):
    # It's easier to store a dict of the possible lookups we want, where
    # the values are the keyword arguments for the actual query.

    query = build_advance_search_query(request)
    title = ""
    # return empty result for empty query
    if len(query) == 0:
        return [], []

    # select one of two approaches for search, by params or best guess
    if 'best' in query:
        title = query['best']
        search_results = search_by_best_guess(query)
    else:
        title = query['q']
        print(title)
        search_results = search_by_params(query)

    return title, search_results, query


def build_advance_search_query(request):
    """Returns a modified copy of request.GET that has no empty value"""
    query = request.GET.copy()

    candidate_queries = {'q', 'isbn', 'author', 'translator', 'publisher', 'category', 'best', 'max_price', 'min_price'}
    # normalize query
    for q in list(query):
        value = query[q]
        value = value.strip()
        if not value:
            del query[q]
        if q not in candidate_queries:
            del query[q]
        else:
            query[q] = value
    return query


def search_by_best_guess(query):
    best = query['best']
    try:
        isbn = int(best)
        return Book.objects.filter(isbn__exact=isbn)
    except ValueError:
        return Book.objects.filter(Q(title__contains=best).__or__(Q(author__contains=best)))


def search_by_params(query):
    qdict = {'q': 'title__contains',
             'isbn': 'isbn__contains',
             'author': 'author__contains',
             'translator': 'translator__contains',
             'publisher': 'publisher__contains',
             'category': 'category__contains',
             }
    # Then we can do this all in one step instead of needing to call
    # 'filter' and deal with intermediate data structures.
    q_objs = [Q(**{qdict[k]: query[k]}) for k in qdict.keys() if k in query]
    print(q_objs)
    search_results = Book.objects.select_related().filter(*q_objs)
    if 'min_price' in query and 'max_price' in query:
        search_results = search_results.filter(price__range=(query['min_price'], query['max_price']))
    return search_results
