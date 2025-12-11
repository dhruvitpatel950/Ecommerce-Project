from django.urls import path
from .views import *
from orders.views import *

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', customer_profile, name='customer_profile'),
    path('dashboard/',seller_dashboard, name='seller_dashboard'),
]