from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['default_address', 'default_city', 'default_postcode', 'default_country']
