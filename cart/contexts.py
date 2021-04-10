from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404 
from artwork.models import Artwork

def cart_content(request):

    cart_items = []
    total = 0
    total_discount = 0
    artwork_count = 0
    cart = request.session.get("cart", {})

    for item_id, quantity in cart.items():
        artwork = get_object_or_404(Artwork, pk=item_id)
        if artwork.price_discounted:
            total_discount += quantity * artwork.price_discounted
        else:
            total += quantity * artwork.price
        artwork_count += quantity
        cart_items.append({
            "item_id": item_id,
            "quantity": quantity,
            "artwork": artwork,
            "total": total,
            "total_discount": total_discount,
        })

    grand_total = total + total_discount

    context = {
        "cart_items": cart_items,
        "total": total,
        "total_discount": total_discount,
        "artwork_count": artwork_count,
        "grand_total": grand_total,
    }

    return context
