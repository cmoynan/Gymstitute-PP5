from django.shortcuts import render

# Create your views here.

def category_list(request):
    categories = [
        {'name': 'Clothing', 'description': 'Shop the latest clothing trends.'},
        {'name': 'Electronics', 'description': 'Find the best electronics.'},
        {'name': 'Workout Plans', 'description': 'Get fit with our workout plans.'},
        {'name': 'Meal Plans', 'description': 'Healthy meal plans for you.'},
    ]
    
    return render(request, 'shop/category_list.html', {'categories': categories})

def clothing_list(request):
    clothes = Clothing.objects.filter(available=True)
    return render(request, 'shop/clothing_list.html', {'clothes': clothes})