from .models import Category, Product
from ketabkhor.models import VitrinLinks


def categories(request):
    return {
        'mainCategories': Category.objects.all()  # todo order
    }


def new_products(request):
    return {
        'newProducts': Product.objects.order_by('-id')[:12]
    }


def get_vitrin_links(request):
    return {
        'vitrins': VitrinLinks.objects.order_by('id')[:5]
    }
