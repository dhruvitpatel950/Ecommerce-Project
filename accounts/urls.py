from django.urls import path
from .views import *

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/',profile_view, name='profile'),
    path('approval-pending/', approval_pending, name='approval_pending'),
    path('blocked/', blocked, name='blocked'),
]