from functools import wraps
from django.shortcuts import redirect, get_object_or_404
from .models import Product

def seller_product_owner_required(view_func):
    @wraps(view_func)
    def wrapper(request, slug, *args, **kwargs):
        product = get_object_or_404(Product, slug=slug, seller=request.user)
        return view_func(request, slug=slug, *args, **kwargs)
    return wrapper
    