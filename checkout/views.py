from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_content

import stripe 

# Create your views here.

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        cart = request.session.get('cart', {})

        form_data = {
            "full_name": request.POST["full_name"],
            "full_name": request.POST["full_name"],
            "full_name": request.POST["full_name"],
            "full_name": request.POST["full_name"],
            "full_name": request.POST["full_name"],
            "full_name": request.POST["full_name"],
        }   
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There are no items in your cart")
            return redirect(reverse('artwork'))

        current_cart = cart_content(request)
        total = current_cart["grand_total"]
        stripe_total = round(total*100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            )

        order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)