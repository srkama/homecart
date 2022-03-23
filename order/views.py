from django.shortcuts import render, redirect
from django.contrib import messages
from cart.models import Cart
from .forms import PaymentForm
from .models import Order
# Create your views here.
# Checkout cart (GET, POST)
# payment (GET, POST)

def checkout(request):
    cart_id = request.session.get('cart')
    if request.method== 'POST':
        order_id = request.session.get('order')
        order = Order.objects.get(id=order_id)
        order.shipping_address = request.POST.get('shipping_address')
        order.delivery_address = request.POST.get('delivery_address')
        order.save()
        return redirect('/payment')
    else:
        cart_id = request.session.get('cart')
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
            order = Order.objects.create_order(cart)
            request.session['order'] = order.id
            return render(request, 'checkout.html', {'order': order})
    return redirect('/')


def payment(request):
    order_id = request.session.get('order')
    if order_id:
        if request.method == 'POST':
            messages.success(request, "payment is successful! order completed!")
            request.session['order'] = None
            request.session['cart'] = None
        else:
            order = Order.objects.get(id=order_id)
            payment_form = PaymentForm()
            return render(request, 'payment.html', {'order': order, 'form': payment_form})
    return redirect('/')