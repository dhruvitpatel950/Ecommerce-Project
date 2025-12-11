from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import blocked_user_required
from products.models import Product
from accounts.models import City
from .models import Order, OrderItem
from .forms import BuyForm
from django.contrib import messages
@login_required
@blocked_user_required
def buy_product(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    
    if request.method == 'POST':
        form = BuyForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            city = form.cleaned_data['city']
            
            if product.stock < quantity:
                form.add_error('quantity', "Not enough stock available.")
                return render(request, 'orders/buy_product.html', {'form': form, 'product': product})
            
            if product.available_in.exists() and not product.available_in.filter(id=city.id).exists():
                form.add_error('city', f"Sorry! This product is not available for delivery in {city.name}.")
                return render(request, 'orders/buy_product.html', {'form': form, 'product': product})
            
            product.stock -= quantity
            product.save()

            total_cost = product.price * quantity

            order = Order.objects.create(
                customer=request.user,
                address=form.cleaned_data['address'],
                phone=form.cleaned_data['phone'],
                total_amount=total_cost  
            )
            
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
            )

            return redirect('customer_profile')
    else:
        initial_data = {'quantity': 1}
        if request.user.city:
            initial_data['city'] = request.user.city
            
        form = BuyForm(initial=initial_data)

    return render(request, 'orders/buy_product.html', {'form': form, 'product': product})

def check_availability(request, slug):
    product = get_object_or_404(Product, slug = slug)
    if request.method == 'POST':
        city_id = request.POST.get('city_id')

        if not city_id:
            messages.error(request, "Please select a city first.")
            return redirect('product_detail', slug=slug)
        
        selected_city = get_object_or_404(City, id = city_id)

        if product.available_in.filter(id=city_id).exists():
            messages.success(request, f"Yay! {product.name} is available in {selected_city.name}!")
        else:
            messages.error(request, f"Sorry, {product.name} is NOT available in {selected_city.name}.")
            
    return redirect('product_detail', slug=slug)