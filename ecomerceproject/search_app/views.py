from django.shortcuts import render
from shop.models import Product
from django.db.models import Q


def searchResults(request):
    query = None
    products = None
    if 'q' in request.GET:
        query = request.GET.get('q').format()
        products = Product.objects.all().filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'search.html', {'query': query, 'products': products, })
