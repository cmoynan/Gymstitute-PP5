from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import category_list, clothing_list
from . import views

urlpatterns = [
    path('', category_list, name='category_list'),
    path('clothing/', views.clothing_list, name='clothing_list'),
]