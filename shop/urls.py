from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import category_list
from shop import views

urlpatterns = [
    path('', category_list, name='category_list'),
    path('categories/', views.category_list, name='category_list'),
    path('clothing/<int:category_id>/', views.clothing_list, name='clothing_list'),
]