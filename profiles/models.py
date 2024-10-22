from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """A user profile model to store delivery details."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_address = models.CharField(max_length=255, blank=True)
    default_city = models.CharField(max_length=50, blank=True)
    default_postcode = models.CharField(max_length=20, blank=True)
    default_country = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username
