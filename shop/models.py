from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Clothing(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='clothing_items')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='clothing_images/', blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Electronic(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='electronic_items')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='electronic_images/', blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name