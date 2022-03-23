from django.shortcuts import render, redirect
from cart.models import Cart

# Create your views here.
def add_to_cart(request, product_id):
    cart = Cart.objects.get_or_new_cart(request)
    cart.add_product(product_id)
    return redirect("/view-cart")


def view_cart(request):
    cart = Cart.objects.get_or_new_cart(request)
    return render(request, 'cart.html', {'cart': cart})