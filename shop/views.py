from django.shortcuts import render, get_object_or_404
from .models import Category, Clothing


# Create your views here.

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'shop/category_list.html', {'categories': categories})
    
    return render(request, 'shop/category_list.html', {'categories': categories})

def clothing_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    clothing_items = Clothing.objects.filter(category=category)
    return render(request, 'shop/clothing_list.html', {'category': category, 'clothing_items': clothing_items})

def electronic_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    electronic_items = Electronic.objects.filter(category=category)
    return render(request, 'shop/electronic_list.html', {'category': category, 'electronic_items': clothing_items})