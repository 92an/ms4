from django.contrib import admin
from .models import Artwork, Medium

# Register your models here.
class ArtworkAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "medium",
        "price",
        "image",
    )

    ordering = ("title", "title")

class MediumAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )

admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Medium, MediumAdmin)
