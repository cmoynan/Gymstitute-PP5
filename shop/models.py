from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('clothing', 'Clothing'),
        ('electronics', 'Electronics'),
        ('workout', 'Workout Plan'),
        ('meal', 'Meal Plan'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='products/')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
