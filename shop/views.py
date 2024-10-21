from django.shortcuts import render, get_object_or_404
from .models import Category, Clothing, Electronic, Workout, Meal

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'shop/category_list.html', {'categories': categories})

def clothing_list(request, id):
    category = get_object_or_404(Category, id=id)
    clothing_items = category.clothing_items.all()
    return render(request, 'shop/clothing_list.html', {'category': category, 'clothing_items': clothing_items})

def electronic_list(request, id):
    category = get_object_or_404(Category, id=id)
    electronic_items = category.electronic_items.all()
    return render(request, 'shop/electronic_list.html', {'category': category, 'electronic_items': electronic_items})

def workout_list(request, id):
    category = get_object_or_404(Category, id=id)
    workout_items = category.workout_items.all()
    return render(request, 'shop/workout_list.html', {'category': category, 'workout_items': workout_items})

def meal_list(request, id):
    category = get_object_or_404(Category, id=id)
    meal_items = category.meal_items.all()
    return render(request, 'shop/meal_list.html', {'category': category, 'meal_items': meal_items})
