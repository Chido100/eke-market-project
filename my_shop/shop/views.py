from django.shortcuts import render, get_object_or_404
from .models import Product, Category


# View list of products
def product_list(request):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


# View product details
def product_detail(request, product_id, slug):
    product = get_object_or_404(Product, id=product_id, slug=slug, avaialble=True)
    return render(request, 'shop/product/detail.html', {'product': product})