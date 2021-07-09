from django import forms
from .models import Artwork, Medium

class ArtworkForm(forms.ModelForm):

    class Meta:
        model = Artwork
        fields = '__all__'
