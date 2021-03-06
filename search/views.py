from django.db.models import Q
from django.http import Http404
from django.shortcuts import render

from product.models import Product


def search(request):
    # try:
    title, results, query = advanced_search(request)
    # except Exception:
    #     raise Http404

    if not results:
        return render(request, 'search/advanced-search-404.html', {
            'title': title})

    return render(request, 'search/advanced-search.html', {
        'title': title,
        'products': results,
        'form_data': query
    })


def advanced_search(request):
    # It's easier to store a dict of the possible lookups we want, where
    # the values are the keyword arguments for the actual query.

    query = build_advance_search_query(request)

    title = ""
    # return empty result for empty query
    if len(query) == 0:
        return [], [], []

    # select one of two approaches for search, by params or best guess
    if 'best' in query:
        title = query['best']
        search_results = search_by_best_guess(query)
    else:
        # get first item in query as title
        title = next(iter(query.values()))

        search_results = search_by_params(query)

    return title, search_results, query


def build_advance_search_query(request):
    """Returns a modified copy of request.GET that has no empty value"""
    query = request.GET.copy()
    candidate_queries = {'q', 'description', 'category', 'best', 'max_price', 'min_price'}
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
    # try:
    #     isbn = int(best)
    #     return Product.objects.filter(isbn__exact=isbn)
    # except ValueError:
    return Product.objects.filter(Q(title__contains=best).__or__(Q(description__contains=best)))


def search_by_params(query):
    qdict = {'q': 'title__contains',
             'description': 'description__contains',
             'category': 'category__title__contains',
             }
    # Then we can do this all in one step instead of needing to call
    # 'filter' and deal with intermediate data structures.
    q_objs = [Q(**{qdict[k]: query[k]}) for k in qdict.keys() if k in query]
    search_results = Product.objects.select_related().filter(*q_objs)

    if 'min_price' in query and 'max_price' in query:
        search_results = search_results.filter(price__range=(query['min_price'], query['max_price']))
    elif 'min_price' in query:
        search_results = search_results.filter(price__gte=query['min_price'])
    elif 'max_price' in query:
        search_results = search_results.filter(price__lte=query['max_price'])

    return search_results
