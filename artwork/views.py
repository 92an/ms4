from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Artwork, Medium
from .forms import ArtworkForm

# Create your views here.


def artwork(request):
    """A view of the artwork for sale, as well as sorting and filtering"""

    artworks = Artwork.objects.all()
    query = None
    mediums = None

    if request.GET:
        if "medium" in request.GET:
            mediums = request.GET["medium"].split(",")
            artworks = artworks.filter(medium__name__in=mediums)
            mediums = Medium.objects.filter(name__in=mediums)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "you need to enter something into the search bar")
                return redirect(reverse("artwork"))

            queries = Q(title__icontains=query) | Q(description__icontains=query)
            artworks = artworks.filter(queries)

    context = {
        "artworks": artworks,
        "search_term": query,
        "current_medium": mediums,
    }

    return render(request, "artwork/artwork.html", context)


def artwork_detail(request, artwork_id):
    """A detailed view of a product"""

    artworks = get_object_or_404(Artwork, pk=artwork_id)

    context = {
        "artworks": artworks,
    }

    return render(request, "artwork/artwork_detail.html", context)

def add_artwork(request):
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artworks = form.save()
            messages.success(request, 'Successfully added artwork!')
            return redirect(reverse('artwork_detail', args=[artworks.id]))
        else:
            messages.error(request, 'Failed to add artwork. Ensure that the form is valid.')
    else:
        form = ArtworkForm()
        template = "artwork/add_artwork.html"
        context = {
            "form": form,
        }

    return render(request, template, context)

def edit_artwork(request, artwork_id):
    artworks = get_object_or_404(Artwork, pk=artwork_id)
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES, instance=artworks)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated artwork!')
            return redirect(reverse('artwork_detail', args=[artworks.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ArtworkForm(instance=artworks)
        messages.info(request, f"You are editing {artworks.title}")

    template = "artwork/edit_artwork.html"
    context = {
        "form": form,
        "artworks": artworks,
    }

    return render(request, template, context)