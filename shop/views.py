from django.shortcuts import render
from .models import Product

# Create your views here.



# View to display the product list by category
def product_list(request, category=None):
    if category:
        products = Product.objects.filter(category=category, available=True)
    else:
        products = Product.objects.filter(available=True)
    return render(request, 'shop/product_list.html', {'products': products, 'category': category})

# View to display product details
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})
