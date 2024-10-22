from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm

def profile(request):
    """ Display the user's profile. """
    # Get the user profile based on the logged-in user
    profile = get_object_or_404(UserProfile, user=request.user)

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

    # Render the profile template with the form
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'on_profile_page': True  # Optional: to indicate we are on the profile page
    }

    return render(request, template, context)
