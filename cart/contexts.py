from django.conf import settings
from django.shortcuts import get_object_or_404 
from artwork.models import Artwork

def cart_content(request):

    cart_items = []
    total = 0
    artwork_count = 0
    cart = request.session.get("cart", {})

    for item_id, quantity in cart.items():
        artwork = get_object_or_404(Artwork, pk=item_id)
        total += quantity * artwork.price
        artwork_count += quantity
        cart_items.append({
            "item_id": item_id,
            "quantity": quantity,
            "artwork": artwork,
        })

    grand_total = total

    context = {
        "cart_items": cart_items,
        "total": total,
        "artwork_count": artwork_count,
        "grand_total": grand_total,
    }

    return context
    