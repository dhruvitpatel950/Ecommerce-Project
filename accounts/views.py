from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib import messages
from .decorators import blocked_user_required
from .models import CustomUser
from products.models import Product
from orders.models import OrderItem


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            role = form.cleaned_data['role']

            if role == 'Customer':
                user.is_approved = True

            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('login')
        
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})    

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, 'invalid credetials')
            return redirect('login')
        
        if user.is_blocked:
            messages.error(request, 'user is blocked')
            return redirect('login')
        
        if user.role == 'Seller' and not user.is_approved:
            messages.error(request, 'approval is pending')
            return redirect('login')
        
        login(request, user)

        if user.role == 'Customer':
            return redirect('product_list')
        elif user.role == 'Seller':
            return redirect('seller_dashboard')
        
        return redirect('profile')
    
    return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def seller_dashboard(request):
    products = Product.objects.filter(seller=request.user)
    return render(request, 'accounts/seller_dashboard.html', {
        'products': products
    })

@login_required
def customer_profile(request):
    purchased_items = OrderItem.objects.filter(order__customer=request.user)

    return render(request, 'accounts/customer_profile.html', {
        'user': request.user,
        'purchased_items': purchased_items,
    })

            

