from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from bag.models import Bag, BagItem
from .models import Order, OrderItem
from django.db import transaction


# Create your views here.

@login_required
@transaction.atomic
def create_order(request):
    bag = get_object_or_404(Bag, user=request.user)
    items = bag.items.all()  # Retrieve all items in the bag

    # Calculate the grand total by summing the price * quantity of each item
    grand_total = sum(item.product.price * item.quantity for item in items)

    if request.method == 'POST':
        # Create the order for the user
        order = Order.objects.create(user=request.user)
        
        # Add each item from the bag to the order
        for item in items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        
        # Clear the bag after creating the order
        bag.items.all().delete()
        
        # Redirect to the order success page
        return redirect('checkout:order_success', order_id=order.id)

    # Render the checkout page with bag items and grand total
    return render(request, 'checkout/create_order.html', {
        'bag': bag,
        'items': items,
        'grand_total': grand_total,
    })

@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'checkout/order_success.html', {'order': order})


