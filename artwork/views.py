from django.shortcuts import render
from .models import Artwork

# Create your views here.


def artwork(request):
    """A view of the artwork for sale, as well as sorting and filtering"""

    artworks = Artwork.objects.all()

    context = {
        "artworks": artworks,
    }

    return render(request, "artwork/artwork.html", context)
