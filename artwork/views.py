from django.shortcuts import render, get_object_or_404
from .models import Artwork

# Create your views here.


def artwork(request):
    """A view of the artwork for sale, as well as sorting and filtering"""

    artworks = Artwork.objects.all()

    context = {
        "artworks": artworks,
    }

    return render(request, "artwork/artwork.html", context)


def artwork_detail(request, artwork_id):
    """A detailed view of a product"""

    artworks = get_object_or_404(Artwork, pk=artwork_id)

    context = {
        "artworks": artworks,
    }

    return render(request, "artwork/artwork_detail.html", context)
