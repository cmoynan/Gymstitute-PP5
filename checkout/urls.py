from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
     path('order-confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
]