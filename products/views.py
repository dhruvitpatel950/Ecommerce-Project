from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from accounts.models import State,City
from django.db.models import Q
from .forms import ProductForm  
from accounts.decorators import blocked_user_required
from .decorators import seller_product_owner_required

def product_list(request):
    query = request.GET.get('q')
    category_products = {}
    search_results = None
    is_search = False
    
    if query:
        is_search = True
        search_results = Product.objects.filter(Q(name__icontains = query) | Q(description__icontains = query), is_active = True)
    else:
        categories = Category.objects.filter(is_active = True, products__isnull = False).distinct()
        for category in categories:
            products = category.products.filter(is_active = True)
            if products.exists():
                category_products[category] = products

    return render(request,'products/product_list.html',{
        'category_products':category_products, 
        'search_results': search_results,
        'is_search': is_search,
        'query': query
        })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    states = State.objects.prefetch_related('cities').all()

    return render(request, 'products/product_detail.html', {'product': product, 'states': states})

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug, is_active=True)
    products = category.products.filter(is_active=True)
    return render(request, 'products/category_products.html', {
        'category': category,
        'products': products
    })

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('seller_dashboard')
    else:
        form = ProductForm()

    return render(request, 'products/add_product.html',{'form':form})

@login_required
@seller_product_owner_required
@blocked_user_required        
def edit_product(request, slug):
    product = get_object_or_404(Product, slug=slug, seller=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('seller_dashboard')
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/add_product.html', {'form': form, 'product': product})

@login_required
@blocked_user_required
@seller_product_owner_required
def delete_product(request, slug):
    product = get_object_or_404(Product, slug=slug, seller=request.user)
    if request.method == 'POST':
        product.delete()
        return redirect('seller_dashboard')
    return render(request, 'products/delete_product.html', {'product': product})




