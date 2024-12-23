from django.urls import path
from .views import *

urlpatterns = [
  path('cart', cartView, name='cart'),
]