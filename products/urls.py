from django.urls import path
from .views import *

urlpatterns = [
    path('', product_list, name='product_list'),
    path('add/', add_product, name='add_product'),
    path('<slug:slug>/', product_detail, name='product_detail'),
    path('category/<slug:slug>/', category_products, name='category_products'),
    path('<slug:slug>/edit/', edit_product, name='edit_product'),
    path('<slug:slug>/delete/', delete_product, name='delete_product'),
]
