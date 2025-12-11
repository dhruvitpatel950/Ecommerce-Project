from django.urls import path
from .views import *

urlpatterns = [
    path('buy/<slug:slug>/', buy_product, name='buy_product'),
    path('check-availability/<slug:slug>/', check_availability, name='check_availability'),
]