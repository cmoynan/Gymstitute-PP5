from django.shortcuts import render, redirect, get_object_or_404
from .models import Bag, BagItem
from shop.models import Product

# Create your views here.


def get_or_create_bag(user):
    bag, created = Bag.objects.get_or_create(user=user)
    return bag

def add_to_bag(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    bag = get_or_create_bag(request.user)
    bag_item, created = BagItem.objects.get_or_create(bag=bag, product=product)

    if not created:
        bag_item.quantity += 1
        bag_item.save()

    return redirect('shop:product_detail', product_id=product.id)

def view_bag(request):
    bag = get_or_create_bag(request.user)
    total_sum = sum(item.product.price * item.quantity for item in bag.items.all())
    return render(request, 'bag/bag.html', {'bag': bag, 'grand_total': total_sum})


def remove_from_bag(request, item_id):
    bag_item = get_object_or_404(BagItem, id=item_id)
    bag_item.delete()
    return redirect('bag:view_bag')