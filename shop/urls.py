from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import category_list
from shop import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('clothing/<int:id>/', views.clothing_list, name='clothing_list'),
    path('electronics/<int:id>/', views.electronic_list, name='electronic_list'),
    path('workouts/<int:id>/', views.workout_list, name='workout_list'),
    path('meals/<int:id>/', views.meal_list, name='meal_list'),
]