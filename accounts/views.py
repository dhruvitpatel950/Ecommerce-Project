from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib import messages
from .decorators import blocked_user_required
from .models import User

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            role = form.cleaned_data['role']

            if role == 'Seller':
                user.is_approved = False
            else:
                user.is_approved = True

            user.set_password(form.cleaned_data['password'])
            user.save()

            if role == 'Seller':
                return redirect('approval_Pending')
            
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
            return redirect('blocked')
        
        if user.role == 'Seller' and not user.is_approved:
            return redirect('approval_pending')
        
        login(request, user)

        if user.role == 'Customer':
            return redirect('product_list')
        elif user.role == 'Seller':
            return redirect('seller_dashboard')
        
        return redirect('profile')
    
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
@blocked_user_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

def approval_pending(request):
    return render(request, 'accounts/approval_pending.html')

def blocked(request):
    return render(request, 'accounts/blocked.html')

            

