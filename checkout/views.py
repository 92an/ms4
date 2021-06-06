from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There are no items in your cart")
        return redirect(reverse('artwork'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IzLngLcyLgSgJ3NvVWvR6YfXLg4RyEpzDnJc5CBRjBJPaEe7CAWLmwoVjvTnARyyZodhBhyKSSEcl3eP8Ye9Oji00Mnkcq3nE',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)