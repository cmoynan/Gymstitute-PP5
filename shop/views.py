from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'shop/category_list.html', {'categories': categories})

def product_list(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = category.products.filter(available=True)
    return render(request, 'shop/product_list.html', {'category': category, 'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})    

def product_list_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'shop/product_list.html', {
        'category': category,
        'products': products,
    })
