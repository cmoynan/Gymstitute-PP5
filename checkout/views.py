from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from bag.models import Bag, BagItem
from .models import Order, OrderItem
from django.db import transaction


# Create your views here.

@login_required
@transaction.atomic
@login_required
def create_order(request):
    bag = get_object_or_404(Bag, user=request.user)
    items = bag.items.all() 

    if request.method == 'POST':
        # Logic for creating the order
        order = Order.objects.create(user=request.user) 
        

        return render(request, 'checkout/order_success.html', {'order': order})

    # For GET requests, render the checkout page with bag items
    return render(request, 'checkout/create_order.html', {'bag': bag, 'items': items})

