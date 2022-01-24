from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category

# Create your views here.
def all_products(request):
    """A view to show all products, including sorting and search categories"""

    products = Product.objects.all()
    categories = Category.objects.all
    query = None
    search_categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
                search_categories = request.GET['category'].split(',')
                products = products.filter(category__name__in=search_categories)
                search_categories = Category.objects.filter(name__in=search_categories)
    
        if 'q' in request.GET:            
            query = request.GET['q']
            if not query:
                messages.error(request, 'You did not enter a search criteria')
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    
    context = {
        'products': products,
        'search_term': query,
        'current_categories': search_categories,
        'categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show an individual product"""

    product = get_object_or_404(Product, pk=product_id)
    categories = Category.objects.all

    # if request.GET:
    
    context = {
        'product': product,
        'categories': categories,
    }

    return render(request, 'products/product_detail.html', context)