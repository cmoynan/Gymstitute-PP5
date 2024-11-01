from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/order/<str:order_number>/', views.order_detail, name='order_detail'),
]