from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import CartItem
from .models import WishlistItem



# 1. Product Listing View
def product_list_view(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'store/product_list.html', {'products': products})

# 2. Product Detail View
def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

# 3. Product Upload View (Only seller)
@login_required
def product_upload_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('store:product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'store/upload.html', {'form': form})



# Add to cart view
@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    CartItem.objects.get_or_create(user=request.user, product=product)
    return redirect('store:cart')

# Cart page
@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'store/cart.html', {'cart_items': cart_items})

# Remove from cart
@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(CartItem, pk=pk, user=request.user)
    item.delete()
    return redirect('store:cart')

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    CartItem.objects.get_or_create(user=request.user, product=product)
    return redirect('store:cart')


@login_required
def wishlist_view(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'store/wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def add_to_wishlist(request, pk):
    product = get_object_or_404(Product, pk=pk)
    WishlistItem.objects.get_or_create(user=request.user, product=product)
    return redirect('store:wishlist')

@login_required
def remove_from_wishlist(request, pk):
    item = get_object_or_404(WishlistItem, pk=pk, user=request.user)
    item.delete()
    return redirect('store:wishlist')
