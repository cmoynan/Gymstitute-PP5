from django.contrib import admin
from .models import Category, Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available', 'is_subscription', 'subscription_price', 'subscription_cycle')
    list_filter = ('category', 'available', 'is_subscription')
    search_fields = ('name', 'description')

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
