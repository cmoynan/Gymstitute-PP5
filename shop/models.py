from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    available = models.BooleanField(default=True)
    is_subscription = models.BooleanField(default=False)
    subscription_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    subscription_cycle = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
