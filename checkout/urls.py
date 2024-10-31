# checkout/urls.py
from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('create_order/', views.create_order, name='create_order'),
]
