
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib import messages

# READ - List products
def product_list(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})

# CREATE
def product_create(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        image_url = request.POST['image_url']

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            image_url=image_url
        )
        messages.success(request, "Product added successfully!")
        return redirect("product_list")
    return render(request, "product_form.html")

# UPDATE
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.image_url = request.POST['image_url']
        product.save()
        messages.success(request, "Product updated successfully!")
        return redirect("product_list")
    return render(request, "product_form.html", {"product": product})

# DELETE
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, "Product deleted successfully!")
    return redirect("product_list")


# add to cart
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)

    cart = request.session.get('cart', {})

    # if product already in cart, increase qty
    if str(pk) in cart:
        cart[str(pk)]['quantity'] += 1
    else:
        cart[str(pk)] = {
            'name': product.name,
            'price': float(product.price),
            'image_url': product.image_url,
            'quantity': 1
        }

    request.session['cart'] = cart
    return redirect('cart_detail')

# 🛒 View Cart
def cart_detail(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'cart.html', {'cart': cart, 'total': total})

# 🛒 Remove item
def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        del cart[str(pk)]
        request.session['cart'] = cart
    return redirect('cart_detail')

# 🛒 Clear cart
def clear_cart(request):
    request.session['cart'] = {}
    return redirect('cart_detail')
# decrease qty
def increase_quantity(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        cart[str(pk)]['quantity'] += 1
    request.session['cart'] = cart
    return redirect('cart_detail')

def decrease_quantity(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart and cart[str(pk)]['quantity'] > 1:
        cart[str(pk)]['quantity'] -= 1
    request.session['cart'] = cart
    return redirect('cart_detail')