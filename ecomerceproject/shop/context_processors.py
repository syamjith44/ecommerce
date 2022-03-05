from django.shortcuts import get_object_or_404

from .models import Category, Product


def menu_links(request):

    category_links = Category.objects.all()
    product_links = Product.objects.all().filter(available=True, )
    return dict(category_links=category_links, product_links=product_links)
