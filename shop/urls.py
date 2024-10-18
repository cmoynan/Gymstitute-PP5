from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<str:category>/', views.product_list, name='product_list_by_category'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]