from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order

def profile(request):
    """Display the user's profile along with their order history."""
    # Get the user profile based on the logged-in user
    profile = get_object_or_404(UserProfile, user=request.user)

    # Fetch all orders made by the user
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    if request.method == 'POST':
        # If the form is submitted, bind the data to the form
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()  # Save the updated profile
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        # If it's a GET request, populate the form with the current profile data
        form = UserProfileForm(instance=profile)

    # Render the profile template with the form and orders
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True  # Optional: to indicate we are on the profile page
    }

    return render(request, template, context)

def order_detail(request, order_number):
    """ Display a single order's details """
    order = get_object_or_404(Order, order_number=order_number, user=request.user)

    template = 'profiles/order_detail.html'
    context = {
        'order': order,
    }

    return render(request, template, context)    