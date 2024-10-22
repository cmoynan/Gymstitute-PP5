from django.shortcuts import render
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def profile(request):
    """Display and update the user's profile."""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        # Your form processing logic here (if applicable)
        pass
    else:
        # Just display the profile
        pass

    return render(request, 'profiles/profile.html', {'profile': profile})