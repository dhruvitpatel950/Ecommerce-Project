from django.shortcuts import redirect
from functools import wraps

def blocked_user_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_blocked:
            return redirect('blocked')  
        return view_func(request, *args, **kwargs)
    return wrapper
