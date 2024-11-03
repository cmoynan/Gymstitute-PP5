from django.db import models
from django.conf import settings
from bag.models import Bag, BagItem
from shop.models import Product
from profiles.models import UserProfile
import uuid

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    order_number = models.CharField(max_length=32, unique=True, blank=True, null=False)

    full_name = models.CharField(max_length=100, default="John Doe")
    email = models.EmailField(default="example@example.com")
    phone_number = models.CharField(max_length=20, blank=True, null=True, default="000-000-0000")
    street_address1 = models.CharField(max_length=80, default="123 Default St")
    street_address2 = models.CharField(max_length=80, blank=True, default="")
    town_or_city = models.CharField(max_length=40, default="Default City")
    county = models.CharField(max_length=40, blank=True, default="")
    postcode = models.CharField(max_length=20, blank=True, default="")
    country = models.CharField(max_length=40, default="United States")

    def save(self, *args, **kwargs):
        if not self.order_number:
            # Generate a unique 8-character order number
            self.order_number = str(uuid.uuid4().hex[:8]).upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.order_number} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in order {self.order.order_number}"


