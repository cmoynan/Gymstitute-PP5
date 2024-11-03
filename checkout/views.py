from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from bag.models import Bag
from .models import Order, OrderItem
from .forms import CheckoutForm
from django.db import transaction
import stripe


# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
@transaction.atomic
def checkout(request):
    bag = get_object_or_404(Bag, user=request.user)
    items = bag.items.all()
    grand_total = sum(item.product.price * item.quantity for item in items)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            # Save order items
            for item in items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )

            # Create Stripe Payment Intent
            intent = stripe.PaymentIntent.create(
                amount=int(grand_total * 100),  # Amount in cents
                currency='usd',
            )

            # Save payment intent ID to the order and set client secret
            order.payment_intent_id = intent.id
            order.save()

            # Clear the bag
            bag.items.all().delete()

            # Redirect to order confirmation
            return redirect('checkout:order_confirmation', order_id=order.id)
    else:
        form = CheckoutForm()

    return render(request, 'checkout/checkout.html', {
        'bag': bag,
        'items': items,
        'grand_total': grand_total,
        'form': form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret if 'intent' in locals() else None,
    })


@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    # Confirm payment status and update order if necessary
    if order.payment_intent_id:
        payment_intent = stripe.PaymentIntent.retrieve(order.payment_intent_id)
        if payment_intent.status == 'succeeded':
            order.is_paid = True
            order.save()

    return render(request, 'checkout/order_confirmation.html', {'order': order})
