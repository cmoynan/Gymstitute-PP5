from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['default_address', 'default_city', 'default_postcode', 'default_country']
        widgets = {
            'default_address': forms.TextInput(attrs={'placeholder': 'Enter your address', 'class': 'form-control'}),
            'default_city': forms.TextInput(attrs={'placeholder': 'Enter your city', 'class': 'form-control'}),
            'default_postcode': forms.TextInput(attrs={'placeholder': 'Enter your postcode', 'class': 'form-control'}),
            'default_country': forms.TextInput(attrs={'placeholder': 'Enter your country', 'class': 'form-control'}),
        }
