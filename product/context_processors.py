from .models import Category, Product


def categories(request):
    return {
        'mainCategories': Category.objects.all()  # todo order
    }

def newProducts(request):
    return {
        'newProducts': Product.objects.order_by('id')[:12]
    }
